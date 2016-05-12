; Sam Rack
; x86 Daily 9
; 02/13/2015

BITS 16

start:
        ; start prelude ;
	cli
        mov ax, 07C0h
        mov ds, ax
        add ax, 0020h
        mov ss, ax
        mov sp, 1000h
        sti
	cld
	;  end prelude  ;

.again:
	call .readLine
	jmp .again

	jmp $	; infinite loop

; procedure readLine ;
.readLine:
	.loop:
		; put next keyboard item in al
		mov ah, 0
		int 16h

		
		; print that keyboard item for user
		mov ah, 0Eh
		int 10h
		
		; if just read a newline, break from loop
		cmp al, 13
		je .done
		
		; otherwise read the next character
		jmp .loop

	.done:
		; print a newline (ASCII = 0A)
		mov al, 0Ah	
		mov ah, 0Eh
		int 10h
		ret
		

	times 510-($-$$) db 0	; fill remainder of sector with zeros
	dw 0xAA55		; BIOS looks for AA55 at the end of the sector

