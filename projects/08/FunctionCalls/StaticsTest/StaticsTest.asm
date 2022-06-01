//This File is generate by translator.
//Implements by gongqingkui at 126.com

@256
D=A
@SP
M=D//SP=256
@sys.init$ret-add-0//***begin call
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
@sys.init
0;JMP//goto f//***end call sys.init 0
(sys.init$ret-add-0)//return-address
(class1.set)//function class1.set 0
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
@16
M=D//pop 16 0
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
@16
A=A+1
M=D//pop 16 1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 0
@LCL//***begin return
D=M
@class1.set$FRAME
M=D//FRAME=LCL
@5
D=A
@class1.set$FRAME
A=M-D
D=M
@class1.set$RET
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
@class1.set$FRAME
AM=M-1
D=M
@THAT
M=D//THAT=*(FRAME-1)
@class1.set$FRAME
AM=M-1
D=M
@THIS
M=D//THIS=*(FRAME-2)
@class1.set$FRAME
AM=M-1
D=M
@ARG
M=D//ARG=*(FRAME-3)
@class1.set$FRAME
AM=M-1
D=M
@LCL
M=D//LCL=*(FRAME-4)
@class1.set$RET
A=M
0;JMP//goto RET//***over return.
(class1.get)//function class1.get 0
@0
D=A
@16
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push static 0
@1
D=A
@16
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push static 1
@SP
AM=M-1
D=M
A=A-1
M=M-D//sub
@LCL//***begin return
D=M
@class1.get$FRAME
M=D//FRAME=LCL
@5
D=A
@class1.get$FRAME
A=M-D
D=M
@class1.get$RET
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
@class1.get$FRAME
AM=M-1
D=M
@THAT
M=D//THAT=*(FRAME-1)
@class1.get$FRAME
AM=M-1
D=M
@THIS
M=D//THIS=*(FRAME-2)
@class1.get$FRAME
AM=M-1
D=M
@ARG
M=D//ARG=*(FRAME-3)
@class1.get$FRAME
AM=M-1
D=M
@LCL
M=D//LCL=*(FRAME-4)
@class1.get$RET
A=M
0;JMP//goto RET//***over return.
(class2.set)//function class2.set 0
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
@16
M=D//pop 16 0
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
@16
A=A+1
M=D//pop 16 1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 0
@LCL//***begin return
D=M
@class2.set$FRAME
M=D//FRAME=LCL
@5
D=A
@class2.set$FRAME
A=M-D
D=M
@class2.set$RET
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
@class2.set$FRAME
AM=M-1
D=M
@THAT
M=D//THAT=*(FRAME-1)
@class2.set$FRAME
AM=M-1
D=M
@THIS
M=D//THIS=*(FRAME-2)
@class2.set$FRAME
AM=M-1
D=M
@ARG
M=D//ARG=*(FRAME-3)
@class2.set$FRAME
AM=M-1
D=M
@LCL
M=D//LCL=*(FRAME-4)
@class2.set$RET
A=M
0;JMP//goto RET//***over return.
(class2.get)//function class2.get 0
@0
D=A
@16
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push static 0
@1
D=A
@16
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1//push static 1
@SP
AM=M-1
D=M
A=A-1
M=M-D//sub
@LCL//***begin return
D=M
@class2.get$FRAME
M=D//FRAME=LCL
@5
D=A
@class2.get$FRAME
A=M-D
D=M
@class2.get$RET
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
@class2.get$FRAME
AM=M-1
D=M
@THAT
M=D//THAT=*(FRAME-1)
@class2.get$FRAME
AM=M-1
D=M
@THIS
M=D//THIS=*(FRAME-2)
@class2.get$FRAME
AM=M-1
D=M
@ARG
M=D//ARG=*(FRAME-3)
@class2.get$FRAME
AM=M-1
D=M
@LCL
M=D//LCL=*(FRAME-4)
@class2.get$RET
A=M
0;JMP//goto RET//***over return.
(sys.init)//function sys.init 0
@6
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 6
@8
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 8
@class1.set$ret-add-1//***begin call
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
@class1.set
0;JMP//goto f//***end call class1.set 2
(class1.set$ret-add-1)//return-address
@SP
AM=M-1
D=M
@R5
M=D//pop R5 0
@23
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 23
@15
D=A
@SP
A=M
M=D
@SP
M=M+1//push constant 15
@class2.set$ret-add-2//***begin call
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
@class2.set
0;JMP//goto f//***end call class2.set 2
(class2.set$ret-add-2)//return-address
@SP
AM=M-1
D=M
@R5
M=D//pop R5 0
@class1.get$ret-add-3//***begin call
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
@class1.get
0;JMP//goto f//***end call class1.get 0
(class1.get$ret-add-3)//return-address
@class2.get$ret-add-4//***begin call
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
@class2.get
0;JMP//goto f//***end call class2.get 0
(class2.get$ret-add-4)//return-address
(StaticsTest.while)//label StaticsTest.while
@StaticsTest.while
0;JMP//goto StaticsTest.while
