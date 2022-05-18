//This File is generate by translator.
//Implements by gongqingkui at 126.com

@0
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D//pop LCL 0
(BasicLoop.loop_start)//label BasicLoop.loop_start
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push argument 0
@0
D=A
@LCL
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push local 0
@SP
AM=M-1
D=M
A=A-1
M=M+D//add
@SP
AM=M-1
D=M
@LCL
A=M
M=D//pop LCL 0
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push argument 0
@1
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 1
@SP
AM=M-1
D=M
A=A-1
M=M-D//sub
@SP
AM=M-1
D=M
@ARG
A=M
M=D//pop ARG 0
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push argument 0
@SP
AM=M-1
D=M
@BasicLoop.loop_start
D;JNE//if-goto BasicLoop.loop_start
@0
D=A
@LCL
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push local 0
