; x86 Daily 7
; Samantha Rack
; 02/10/15

BITS 16

start:
                        ; this is the prelude, where we set up the data
                        ; and stack segments
        cli             ; turn off interrupts while setting up DS and SS
        mov ax, 07C0h   ; recall that 07C0h is where the bootloader starts
                        ; so, that is the start of the data segment (DS)
        mov ds, ax      ; move AX into DS because we can't set DS directly
                        ; that's all we need to do for the data segment...
                        ; ...now we need to set up the stack
                        ; to do that, we move forward by 512 bytes (the
                        ; size of this bootloader) to get a starting point
                        ; for the stack.
                        ; to do that, we want the stack segment (SS register)
                        ; to point to the end of the bootloader, which is
                        ; the data segment start (07C0h) plus the size of the
                        ; the bootloader.
                        ; but, segments are addressed in multiples of 16
                        ; (called "paragraphs"), so we actually add 512/16=
        add ax, 0020h   ; 32, which is 0020 in hex
        mov ss, ax      ; set the stack segment to 07E0h (07C0h + 0020h)
        mov sp, 1000h   ; set the stack pointer to 4096 bytes (1000h)
                        ; remember that this will grow *down*, towards SS
        sti             ; turn the interrupts back on

	mov ah, 0h	; set function code to 0h, which is the set video mode
	mov al, 13h	; 13h is graphics mode
	int 10h		; issue interrupt to the firmware service

	mov ah, 0Eh	; set function code to 0Eh, which is teletype
	mov al, 53h	; set char register, 53h is for ASCII 'S'
	mov bh, 0h	; set page number, should be 0
	mov bl, 04h	; set color code, 04h is red
	int 10h		; issue interrupt

	mov al, 52h	; set char register, 52h is for ASCII 'R'
	mov bl, 02h	; set a new color
	int 10h		; other values persist, issue interrupt

	mov bl, 06h	; set a new color
	int 10h		; other values persist, issue interrupt

	jmp $

	times 510-($-$$) db 0
	dw 0xAA55	; BIOS looks for AA55 at the end of the sector

