# Assembler

Assembler is a program for converting instructions written in low-level assembly code into relocatable machine code.

Pass-1:
  Define symbols and literals and stoes them in symbol table[symbolCOllection.py] and literal table[literalTable.py] respectively.
  Keep track of location counter[passage.py]
  Process errors[ErrorTable.py]
Pass-2:
  Generate object code by converting symbolic op-code into respective numeric op-code[opcodeTable.py]
  Generate data for literals and look for values of symbols [[p.lst]
