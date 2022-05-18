//This File is generate by translator.
//Implements by gongqingkui at 126.com

@1
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push argument 1
@SP
AM=M-1
D=M
@R3
A=A+1
M=D//pop R3 1
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
@THAT
A=M
M=D//pop THAT 0
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
@THAT
A=M
A=A+1
M=D//pop THAT 1
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
@2
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 2
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
(FibonacciSeries.main_loop_start)//label FibonacciSeries.main_loop_start
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
@FibonacciSeries.compute_element
D;JNE//if-goto FibonacciSeries.compute_element
@FibonacciSeries.end_program
0;JMP//goto FibonacciSeries.end_program
(FibonacciSeries.compute_element)//label FibonacciSeries.compute_element
@0
D=A
@THAT
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push that 0
@1
D=A
@THAT
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push that 1
@SP
AM=M-1
D=M
A=A-1
M=M+D//add
@SP
AM=M-1
D=M
@THAT
A=M
A=A+1
A=A+1
M=D//pop THAT 2
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
M=M+D//add
@SP
AM=M-1
D=M
@R3
A=A+1
M=D//pop R3 1
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
@FibonacciSeries.main_loop_start
0;JMP//goto FibonacciSeries.main_loop_start
(FibonacciSeries.end_program)//label FibonacciSeries.end_program
