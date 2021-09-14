// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm
// Implements: gongqingkui At 126.com

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program BLACKens the screen,
// i.e. writes "BLACK" in every pixel;
// the screen should remain fully BLACK as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "WHITE" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// max
@24575
D=A
@max
M=D
//min
@SCREEN
D=A
@min
M=D
// current
@current
M=D

// color  = WHITE 
@color
M=0

// key = KBD
@KBD
D=M
@key
M=D

//loop
(LOOP)
// current = min
@SCREEN
D=A
@current
M=D 
// color = WHITE
@color
M=0
// key = M[kbd]
@KBD
D=M
@key
M=D
// if key == 0:color = WHITE
@WHITE
D;JEQ
// color = BLACK
@BLACK
0;JMP
// color = WHITE
(WHITE)
@color
M=0
@DRAW
0;JMP
//color = BLACK 
(BLACK)
@color
M=-1
@DRAW
0;JMP

//draw
(DRAW)
//while max - currnet >0:
@current
D=M
@max
D=M-D
@LOOP
D;JLE 
//M[current] = color
@color
D=M
@current
A=M
M=D
//current++
@current
A=M
D=A+1
@current
M=D
// goto DRAW
@DRAW
0;JMP 
