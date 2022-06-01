@261
D=A
@SP
M=D//SP=256
@sys.init
0;JMP
//call sys.init
(add.sum)//function add.sum 0
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
M=M+D//add
@LCL//***begin return
D=M
@add.sum$FRAME
M=D//FRAME=LCL
@5
D=A
@add.sum$FRAME
A=M-D
D=M
@add.sum$RET
M=D//RET=*(FRAME-5)
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D//*ARG=pop()
@ARG
D=M+1
@SP
M=D//SP=ARG+1
@add.sum$FRAME
AM=M-1
D=M
@THAT
M=D//THAT=*(FRAME-1)
@add.sum$FRAME
AM=M-1
D=M
@THIS
M=D//THIS=*(FRAME-2)
@add.sum$FRAME
AM=M-1
D=M
@ARG
M=D//ARG=*(FRAME-3)
@add.sum$FRAME
AM=M-1
D=M
@LCL
M=D//LCL=*(FRAME-4)
@add.sum$RET
A=M
0;JMP//goto RET//***over return.
(sys.init)//function sys.init 0
@1
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 1
@2
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 2
@add.sum$ret-add-0//***begin call
D=A
@SP
A=M
M=D
@SP
M=M+1//push return-address
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1//push LCL
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1//push ARG
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1//push THIS
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1//push THAT
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D//ARG=SP-n-5
@SP
D=M
@LCL
M=D//LCL=SP
@add.sum
0;JMP//goto f//***end call add.sum 2
(add.sum$ret-add-0)//return-address
(SimpleCall.while)//label SimpleCall.while
@SimpleCall.while
0;JMP//goto SimpleCall.while
