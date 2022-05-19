@sys.init
0;JMP//call sys.init
(sys.init)//function sys.init 0
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 4000
@SP
AM=M-1
D=M
@R3
M=D//pop R3 0
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 5000
@SP
AM=M-1
D=M
@R3
A=A+1
M=D//pop R3 1
@sys.main$ret-add-0//***begin call
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
@0
D=D-A
@5
D=D-A
@ARG
M=D//ARG=SP-n-5
@SP
D=M
@LCL
M=D//LCL=SP
@sys.main
0;JMP//goto f//***end call sys.main 0
(sys.main$ret-add-0)//return-address
@SP
AM=M-1
D=M
@R5
A=A+1
M=D//pop R5 1
(NestedCall.loop)//label NestedCall.loop
@NestedCall.loop
0;JMP//goto NestedCall.loop
(sys.main)
@LCL
A=M
M=0//init local 0
A=A+1
M=0//init local 1
A=A+1
M=0//init local 2
A=A+1
M=0//init local 3
A=A+1
M=0//init local 4//function sys.main 5
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 4001
@SP
AM=M-1
D=M
@R3
M=D//pop R3 0
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 5001
@SP
AM=M-1
D=M
@R3
A=A+1
M=D//pop R3 1
@200
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 200
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
M=D//pop LCL 1
@40
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 40
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D//pop LCL 2
@6
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 6
@SP
AM=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
M=D//pop LCL 3
@123
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 123
@sys.add12$ret-add-1//***begin call
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
@sys.add12
0;JMP//goto f//***end call sys.add12 1
(sys.add12$ret-add-1)//return-address
@SP
AM=M-1
D=M
@R5
M=D//pop R5 0
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
@2
D=A
@LCL
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push local 2
@3
D=A
@LCL
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push local 3
@4
D=A
@LCL
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push local 4
@SP
AM=M-1
D=M
A=A-1
M=M+D//add
@SP
AM=M-1
D=M
A=A-1
M=M+D//add
@SP
AM=M-1
D=M
A=A-1
M=M+D//add
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
@sys.main$FRAME
M=D//FRAME=LCL
@sys.main$FRAME
AM=M-1
D=M
@THAT
M=D//THAT=*(FRAME-1)
@sys.main$FRAME
AM=M-1
D=M
@THIS
M=D//THIS=*(FRAME-2)
@sys.main$FRAME
AM=M-1
D=M
@ARG
M=D//ARG=*(FRAME-3)
@sys.main$FRAME
AM=M-1
D=M
@LCL
M=D//LCL=*(FRAME-4)
@sys.main$FRAME
AM=M-1
D=M
@sys.main$RET
M=D//RET=*(FRAME-5)
@sys.main$RET
A=M
0;JMP//goto RET//***over return.
(sys.add12)//function sys.add12 0
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 4002
@SP
AM=M-1
D=M
@R3
M=D//pop R3 0
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 5002
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
@12
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 12
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
@sys.add12$FRAME
M=D//FRAME=LCL
@sys.add12$FRAME
AM=M-1
D=M
@THAT
M=D//THAT=*(FRAME-1)
@sys.add12$FRAME
AM=M-1
D=M
@THIS
M=D//THIS=*(FRAME-2)
@sys.add12$FRAME
AM=M-1
D=M
@ARG
M=D//ARG=*(FRAME-3)
@sys.add12$FRAME
AM=M-1
D=M
@LCL
M=D//LCL=*(FRAME-4)
@sys.add12$FRAME
AM=M-1
D=M
@sys.add12$RET
M=D//RET=*(FRAME-5)
@sys.add12$RET
A=M
0;JMP//goto RET//***over return.
