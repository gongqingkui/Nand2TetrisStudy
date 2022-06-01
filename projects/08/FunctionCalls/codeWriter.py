# This file is implements of 'The elements of computer systems'
# chap 7.Virtual Machine:Stack
# CodeWrite module
# author:gongqingkui AT 126.com
# date:2022-05-12

from parserVMTranslator import commandType,arg2
import os

asm_file = None
jmp_index = 0
current_function_name = None
call_index = 0
segment_map = {'local':'LCL','argument':'ARG','this':'THIS','that':'THAT','temp':'R5','pointer':'R3','static':'16'}
spInc = '@SP\nM=M+1\n'
spDec = '@SP\nM=M-1\n'

def CodeWriter(file_):
    global asm_file
    asm_file = open(file_,'w')
    return asm_file

    
def writeArithmetic(command):
    global jmp_index
    c = command.split(' ')
    if commandType(command) == 'C_ARITHMETIC':
        if c[0] in ['add','sub','and','or']:
            asm_code = '@SP\nAM=M-1\nD=M\nA=A-1\nM=M%sD//%s\n'
            oper = ''
            if c[0] == 'add':
                oper = '+'
            elif c[0] == 'sub':
                oper = '-'
            elif c[0] == 'and':
                oper = '&'
            elif c[0] == 'or':
                oper = '|'
            asm_code = asm_code%(oper,c[0]) 
        if c[0] in ['eq','lt','gt']:
            asm_code = '@SP\nAM=M-1\nD=M\nA=A-1\nMD=M-D//arg1-arg2\n@TRUE_%s\nD;%s\n@SP//begin FALSE\nD=A\n@0\nA=M-1\nM=D\n@CONTINUE_%s\n0;JMP//end FALSE\n(TRUE_%s)//begin TRUE\n@1\nD=-A\n@SP\nA=M-1\nM=D//end TRUE\n(CONTINUE_%s)//%s\n'
            oper = ''
            if c[0] == 'eq':
                oper = 'JEQ'
            elif c[0] == 'lt':
                oper = 'JLT'
            elif c[0] == 'gt':
                oper = 'JGT'
            elif c[0] == 'or':
                oper = '|'
            asm_code = asm_code%(jmp_index,oper,jmp_index,jmp_index,jmp_index,c[0]) 
            jmp_index += 1
        elif c[0] in ['neg','not']:
            #asm_code = '@SP\nA=M-1\nM=%sM//%s\n'
            asm_code = spInc ,'M=%sM//%s\n'
            oper = ''
            if c[0] == 'neg':
                oper = '-'
            elif c[0] == 'not':
                oper = '!'
            asm_code = asm_code%(oper,c[0])
        asm_file.write(asm_code)


def writePushPop(command,segment,index):
    #print(command,segment,index)
    if commandType(command) == 'C_PUSH':
        if segment == 'constant':
            asm_code = '@%s\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1//push constant %s\n'%(index,index)
        if segment in ['temp','static','pointer']:
            asm_code = '@%s\nD=A\n@%s\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1//push %s %s\n'%(index,segment_map[segment],segment,index)
        if segment in ['local','argument','this','that']:
            asm_code = '@%s\nD=A\n@%s\nA=M\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1//push %s %s\n'%(index,segment_map[segment],segment,index)
        asm_file.write(asm_code)
    if commandType(command) == 'C_POP':
        if segment in ['local','argument','this','that']:
            asm_code = '@SP\nAM=M-1\nD=M\n@%s\nA=M\n'%segment_map[segment]
            asm_code += 'A=A+1\n'*index
            asm_code += 'M=D//pop %s %s\n'%(segment_map[segment],index) 
        if segment in ['temp','static','pointer']:
            asm_code = '@SP\nAM=M-1\nD=M\n@%s\n'%segment_map[segment]
            asm_code += 'A=A+1\n'*index
            asm_code += 'M=D//pop %s %s\n'%(segment_map[segment],index) 
        asm_file.write(asm_code) 


def fileBaseName(fname):
    return os.path.basename(fname.name)[:-4]


def writeLabel(command,label):
    if commandType(command) == 'C_LABEL':
        vmFileName = fileBaseName(asm_file)
        label = '%s.%s'%(vmFileName,label)
        asm_code = '(%s)//label %s\n'%(label,label)
        #print(command,label,asm_code)
        asm_file.write(asm_code) 


def writeGoto(command,label):
    if commandType(command) == 'C_GOTO':
        vmFileName = fileBaseName(asm_file)
        label = '%s.%s'%(vmFileName,label)
        asm_code = '@%s\n0;JMP//goto %s\n'%(label,label)
        #print(command,label,asm_code)
        asm_file.write(asm_code) 


def writeIf(command,label):
    if commandType(command) == 'C_IF':
        vmFileName = fileBaseName(asm_file)
        label = '%s.%s'%(vmFileName,label)
        asm_code = '@SP\nAM=M-1\nD=M\n@%s\nD;JNE//if-goto %s\n'%(label,label)
        #print(command,label,asm_code)
        asm_file.write(asm_code) 
        

def writeFunction(command,functionName,numArgs):
    if commandType(command) == 'C_FUNCTION':
        global current_function_name
        current_function_name = functionName
        #vmFileName = fileBaseName(asm_file)
        #functionName = '%s.%s'%(vmFileName,functionName)
        asm_code = '(%s)'%functionName
        if numArgs > 0:
            asm_code += '\n@LCL\nA=M\nM=0//init local 0'
            if numArgs > 1:
                for i in range(numArgs - 1):
                    asm_code += '\nA=A+1\nM=0//init local %d'%(i+1)
                asm_code += '\nD=A+1\n@SP\nM=D\n'
        asm_code += '//function %s %s\n'%(functionName,numArgs)    
        #print(command,functionName,numArgs,asm_code)
        asm_file.write(asm_code) 


def writeCall(command,functionName,numArgs):
    global call_index
    if commandType(command) == 'C_CALL':
        asm_code = '@%s$ret-add-%d//***begin call\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1//push return-address\n'%(functionName,call_index)
        asm_code += '@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1//push LCL\n'
        asm_code += '@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1//push ARG\n'
        asm_code += '@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1//push THIS\n'
        asm_code += '@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1//push THAT\n' 
        asm_code += '@SP\nD=M\n@%s\nD=D-A\n@5\nD=D-A\n@ARG\nM=D//ARG=SP-n-5\n'%numArgs
        asm_code += '@SP\nD=M\n@LCL\nM=D//LCL=SP\n'
        asm_code += '@%s\n0;JMP//goto f//***end call %s %s\n'%(functionName,functionName,numArgs)
        asm_code += '(%s$ret-add-%d)//return-address\n'%(functionName,call_index)

        asm_file.write(asm_code) 
        call_index += 1 
       

def writeReturn(command):
    global current_function_name
    if commandType(command) == 'C_RETURN':
        cfn = current_function_name
        asm_code = '@LCL//***begin return\nD=M\n@%s$FRAME\nM=D//FRAME=LCL\n'%cfn
        asm_code += '@5\nD=A\n@%s$FRAME\nA=M-D\nD=M\n@%s$RET\nM=D//RET=*(FRAME-5)\n'%(cfn,cfn)
        asm_code += '@SP\nM=M-1\nA=M\nD=M\n@ARG\nA=M\nM=D//*ARG=pop()\n'
        asm_code += '@ARG\nD=M+1\n@SP\nM=D//SP=ARG+1\n'
        asm_code += '@%s$FRAME\nAM=M-1\nD=M\n@THAT\nM=D//THAT=*(FRAME-1)\n'%cfn
        asm_code += '@%s$FRAME\nAM=M-1\nD=M\n@THIS\nM=D//THIS=*(FRAME-2)\n'%cfn
        asm_code += '@%s$FRAME\nAM=M-1\nD=M\n@ARG\nM=D//ARG=*(FRAME-3)\n'%cfn
        asm_code += '@%s$FRAME\nAM=M-1\nD=M\n@LCL\nM=D//LCL=*(FRAME-4)\n'%cfn
        asm_code += '@%s$RET\nA=M\n0;JMP//goto RET//***over return.\n'%cfn
        asm_file.write(asm_code) 
        current_function_name = None


def writeHeadBlock():
    asm_file.write('//This File is generate by translator.\n//Implements by gongqingkui at 126.com\n\n')
    writeBootStrap()


def writeBootStrap():
    #this is bootstrap code
    ########## for nestedCall and fibnacciElement
    #asm_file.write('@261\nD=A\n@SP\nM=D//SP=256\n') 
    ########## for simpleCall 
    #asm_file.write('@sys.init\n0;JMP\n//call sys.init\n') 
    ########## for simpleCall 
    ########## for staticTest
    asm_file.write('@256\nD=A\n@SP\nM=D//SP=256\n') 
    writeCall('call','sys.init',0)
    ########## for staticTest
    pass


def close():
    asm_file.close() 
