// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm
// Implements: gongqingkui At 126.com

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

(LOOP)
@1
D=M
@2
M=D+M
@0
M=A-1
@0
D=M
@LOOP
D;JGT
(END)
@END
0;JMP
