//This File is generate by translator.
//Implements by gongqingkui at 126.com

@3030
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 3030
@SP
AM=M-1
D=M
@R3
M=D//pop R3 0
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 3040
@SP
AM=M-1
D=M
@R3
A=A+1
M=D//pop R3 1
@32
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 32
@SP
AM=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D//pop this 2
@46
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 46
@SP
AM=M-1
D=M
@THAT
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D//pop that 6
@0
D=A
@R3
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push temp 0
@1
D=A
@R3
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push temp 1
@SP
AM=M-1
D=M
A=A-1
M=M+D//add
@2
D=A
@THIS
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push this 2
@SP
AM=M-1
D=M
A=A-1
M=M-D//sub
@6
D=A
@THAT
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push that 6
@SP
AM=M-1
D=M
A=A-1
M=M+D//add
