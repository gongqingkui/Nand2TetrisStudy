//This File is generate by translator.
//Implements by gongqingkui at 126.com

@111
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 111
@333
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 333
@888
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 888
@8
D=A
@16
D=A+D
@add
M=D
@SP
AM=M-1
D=M
@add
A=M
M=D//pop temp 8
@3
D=A
@16
D=A+D
@add
M=D
@SP
AM=M-1
D=M
@add
A=M
M=D//pop temp 3
@1
D=A
@16
D=A+D
@add
M=D
@SP
AM=M-1
D=M
@add
A=M
M=D//pop temp 1
@3
D=A
@16
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push temp 3
@1
D=A
@16
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
M=M-D//sub
@8
D=A
@16
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push temp 8
@SP
AM=M-1
D=M
A=A-1
M=M+D//add
