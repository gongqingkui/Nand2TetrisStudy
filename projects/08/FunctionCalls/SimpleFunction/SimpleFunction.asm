//This File is generate by translator.
//Implements by gongqingkui at 126.com

(simplefunction.test)
@LCL
A=M
M=0//init local 0
A=A+1
M=0//init local 1//function simplefunction.test 2
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
@SP
A=M-1
M=!M//not
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
A=A-1
M=M+D//add
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
A=A-1
M=M-D//sub
@SP//***begin return
AM=M-1
D=M
@ARG
A=M
M=D//*ARG=pop()
@ARG
D=M+1
@SP
M=D//SP=ARG+1
@LCL
D=M
@simplefunction.test$FRAME
M=D//FRAME=LCL
@simplefunction.test$FRAME
AM=M-1
D=M
@THAT
M=D//THAT=*(FRAME-1)
@simplefunction.test$FRAME
AM=M-1
D=M
@THIS
M=D//THIS=*(FRAME-2)
@simplefunction.test$FRAME
AM=M-1
D=M
@ARG
M=D//ARG=*(FRAME-3)
@simplefunction.test$FRAME
AM=M-1
D=M
@LCL
M=D//LCL=*(FRAME-4)
@simplefunction.test$FRAME
AM=M-1
D=M
@simplefunction.test$RET
M=D//RET=*(FRAME-5)
@simplefunction.test$RET
A=M
0;JMP//goto RET//return ***over.
