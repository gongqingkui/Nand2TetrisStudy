@sys.init
0;JMP//call sys.init
(main.fibonacci)//function main.fibonacci 0
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
MD=M-D//arg1-arg2
@TRUE_0
D;JLT
@SP//begin FALSE
D=A
@0
A=M-1
M=D
@CONTINUE_0
0;JMP//end FALSE
(TRUE_0)//begin TRUE
@1
D=-A
@SP
A=M-1
M=D//end TRUE
(CONTINUE_0)//lt
@SP
AM=M-1
D=M
@FibonacciElement.if_true
D;JNE//if-goto FibonacciElement.if_true
@FibonacciElement.if_false
0;JMP//goto FibonacciElement.if_false
(FibonacciElement.if_true)//label FibonacciElement.if_true
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
@main.fibonacci$FRAME
M=D//FRAME=LCL
@main.fibonacci$FRAME
AM=M-1
D=M
@THAT
M=D//THAT=*(FRAME-1)
@main.fibonacci$FRAME
AM=M-1
D=M
@THIS
M=D//THIS=*(FRAME-2)
@main.fibonacci$FRAME
AM=M-1
D=M
@ARG
M=D//ARG=*(FRAME-3)
@main.fibonacci$FRAME
AM=M-1
D=M
@LCL
M=D//LCL=*(FRAME-4)
@main.fibonacci$FRAME
AM=M-1
D=M
@main.fibonacci$RET
M=D//RET=*(FRAME-5)
@main.fibonacci$RET
A=M
0;JMP//goto RET//***over return.
(FibonacciElement.if_false)//label FibonacciElement.if_false
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
@main.fibonacci$ret-add-0//***begin call
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
@1
D=D-A
@5
D=D-A
@ARG
M=D//ARG=SP-n-5
@SP
D=M
@LCL
M=D//LCL=SP
@main.fibonacci
0;JMP//goto f//***end call main.fibonacci 1
(main.fibonacci$ret-add-0)//return-address
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
@main.fibonacci$ret-add-1//***begin call
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
@1
D=D-A
@5
D=D-A
@ARG
M=D//ARG=SP-n-5
@SP
D=M
@LCL
M=D//LCL=SP
@main.fibonacci
0;JMP//goto f//***end call main.fibonacci 1
(main.fibonacci$ret-add-1)//return-address
@SP
AM=M-1
D=M
A=A-1
M=M+D//add
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
@None$FRAME
M=D//FRAME=LCL
@None$FRAME
AM=M-1
D=M
@THAT
M=D//THAT=*(FRAME-1)
@None$FRAME
AM=M-1
D=M
@THIS
M=D//THIS=*(FRAME-2)
@None$FRAME
AM=M-1
D=M
@ARG
M=D//ARG=*(FRAME-3)
@None$FRAME
AM=M-1
D=M
@LCL
M=D//LCL=*(FRAME-4)
@None$FRAME
AM=M-1
D=M
@None$RET
M=D//RET=*(FRAME-5)
@None$RET
A=M
0;JMP//goto RET//***over return.
(sys.init)//function sys.init 0
@4
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 4
@main.fibonacci$ret-add-2//***begin call
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
@1
D=D-A
@5
D=D-A
@ARG
M=D//ARG=SP-n-5
@SP
D=M
@LCL
M=D//LCL=SP
@main.fibonacci
0;JMP//goto f//***end call main.fibonacci 1
(main.fibonacci$ret-add-2)//return-address
(FibonacciElement.while)//label FibonacciElement.while
@FibonacciElement.while
0;JMP//goto FibonacciElement.while
