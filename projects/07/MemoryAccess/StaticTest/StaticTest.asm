//This File is generate by translator.

//push constant
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop temp
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
M=D
//pop temp
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
M=D
//pop temp
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
M=D
//push temp
@3
D=A
@16
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push temp
@1
D=A
@16
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//Arithmetic
@SP
AM=M-1
D=M
A=A-1
M=M-D
//push temp
@8
D=A
@16
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//Arithmetic
@SP
AM=M-1
D=M
A=A-1
M=M+D
