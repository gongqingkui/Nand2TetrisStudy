(simplefunction.test)
@LCL
A=M
M=0//init local 0
A=A+1
M=0//init local 1
D=A+1
@SP
M=D
//function simplefunction.test 2
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
@1
D=A
@LCL
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push local 1
@SP
AM=M-1
D=M
A=A-1
M=M+D//add
