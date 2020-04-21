 	section .data
	
	Array dd 10,20,30,40
	a dd 0
	msg db "hello"
	abc db "hi"

	section .bss
	four resd 10

	section .text
	global main
	extern printf

main:
	mov 0, ecx
	mov dword[ four ], a
	mov eax, ecx
lb: xor edx,edx
	mov dword[ four ], eax
	mov ebx, eax
	mov eax, Array	
	add eax, ebx
	push a
	push dword[eax]
	push msg
	call printf
	add esp, 8
	pop a
	inc ecx
	cmp ecx, 3
	jle abc
