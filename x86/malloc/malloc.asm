; Sam Rack
; x86 Flex Points -- malloc
; 02/20/2015

BITS 16

; BUFLOC starts at ss
%define HEAPPTR 200h

start:
	; prelude ;
	cli
        mov ax, 07C0h
        mov ds, ax
	mov es, ax
        add ax, 0020h
        mov ss, ax
        mov sp, 1000h
        sti
	cld

	; initialize the heap pointer 
	mov di, HEAPPTR

	; add one to get the start of the actual heap
	mov al, 2
	
	; store this initial location in heap pointer
	stosb

	; begin command line logic ;
	.again:
		; print the prompt
		mov si, prompt
		call print

		mov al, 16 
		call malloc
		mov di, bx

		; handle a line of input
		;mov di, [HEAPSTART]
		call userInput

		; call echo
		call echo	
	
	.strcmpTrDone:
		jmp .again

	; infinite loop ;
	jmp $	


; malloc
; BEFORE CALLING, SET -- al 
; al is the amount of space desired for allocation
; AFTER CALLING, USE -- bx 
; bx is the location where the newly allocated memory begins
malloc:
	mov di, HEAPPTR
	; set si to current location of end of heap
	mov si, HEAPPTR
	add si, [di]

	; set bx for the return
	mov bx, si

	; set al to new location of end of heap
	add al, [di]

	; store this new location to HEAPPTR
	stosb
	
	ret


; echo
; determines if the user input was for the command echo
;  and prints the remaineder of the input if so 
echo:
	mov di, HEAPPTR
	mov si, [di] 
	mov di, echoS
	call strcmp

	je .echoDo
	jmp .echoDone

	.echoDo:
		; check if there is either a space or newline after echo
		;lodsb
		;cmp al, 20h 
		;je .echoWord
		;cmp al, 0dh
		;je .echoNewLine
		;jmp .echoDone
	
	.echoWord:	
		call print

	.echoNewLine:
		; print a newline (so what is echo-ed is not overwritten by the prompt)
		mov ah, 0Eh
		mov al, 0Ah
		int 10h

	.echoDone:
		ret

; strcmp
; BEFORE CALLING, SET -- ds, si, di
; ds:si is the location of the first byte of the first string 
; es:di is the location of the first byte of the second string
; will set compare byte for je to true if strings are equal
strcmp:
	.strcmpLoop:
		; check if si is null, if yes, then we are done
		mov ax, [si]
		cmp ax, 0
		je .strcmpDone

		; check if di is null
		mov ax, [di]
		cmp ax, 0
		je .strcmpDone

		; do the comparison if neither are null
		cmpsb
		je .strcmpLoop
		jmp .strcmpDone

	.strcmpDone:
		ret

; userInput 
; BEFORE CALLING, SET -- es, di, ax
; es:di is the starting location of the buffer where the bytes
;  typed by the user will be stored
; implements backspace
userInput:
	; save the initial di
	mov ax, di

	.uiLoop:
		; put next keyboard item in al
		mov ah, 0
		int 16h

		; check for backspace
		cmp al, 08h
		je .uiBksp
		jmp .uiNoBksp

	.uiBksp:
		; don't do anything with backspace if nothing written in buffer
		cmp di, ax
		je .uiLoop

		; print first backspace
		mov ah, 0Eh
		int 10h

		; print a space
		mov al, 20h
		int 10h

		; print another backspace
		mov al, 08h
		int 10h

		; move di back so character erased from buffer
		sub di, 01h
		
		; start over with the next input character
		jmp .uiLoop	

	.uiNoBksp:
		; print that keyboard item for user
		mov ah, 0Eh
		int 10h
		
		; store the byte to the heap (es:di)
		stosb
	
		; if just read a newline, break from loop
		cmp al, 13
		je .uiDone
		
		; otherwise read the next character
		jmp .uiLoop

	.uiDone:
		; print a newline (ASCII = 0A)
		mov al, 0Ah	
		mov ah, 0Eh
		int 10h

		; save a null byte at the end of the buffer
		mov al, 0h
		stosb
	
		;mov si, BUFLOC
		;call print
	
		; return to caller
		ret

; print 
; BEFORE CALLING, SET -- ds, si
; ds:si is the location of the first byte that will be printed
print:
	mov ah, 0Eh	; set function code for teletype
	.printLoop:
		; load the next byte to al for printing (also ++si)
		lodsb

		; check if this byte is null, exit if yes
		cmp al, 0
		je .printDone

		; print the byte
		int 10h
		jmp .printLoop
			
	.printDone:
		; return to caller
		ret



;;;;;;;;;;;;;;;;;;;;;
;;      DATA       ;; 
;;;;;;;;;;;;;;;;;;;;;
prompt db '> ', 0
echoS db 'echo', 0
;;;;;;;;;;;;;;;;;;;;;

	; fill in the remaineder of the sector with zeros
	times 510-($-$$) db 0		
	; AA55 at end of sector for BIOS
	dw 0xAA55


