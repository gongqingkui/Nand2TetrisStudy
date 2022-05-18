# This file is implements of 'The elements of computer systems'
# chap 7.Virtual Machine:Stack
# CodeWrite module
# author:gongqingkui AT 126.com
# date:2022-05-12

from parserVMTranslator import commandType,arg2
import os

asm_file = None
jmp_index = 0
segment_map = {'local':'LCL','argument':'ARG','this':'THIS','that':'THAT','temp':'R5','pointer':'R3','static':'16'}

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
            asm_code = '@SP\nAM=M-1\nD=M\nA=A-1\nMD=M-D\n@TRUE_%s\nD;%s\n@SP\nD=A\n@0\nA=M-1\nM=D\n@CONTINUE_%s\n0;JMP\n(TRUE_%s)\n@1\nD=-A\n@SP\nA=M-1\nM=D\n(CONTINUE_%s)//%s\n'
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
            asm_code = '@SP\nA=M-1\nM=%sM//%s\n'
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
            asm_code = '@%s\nD=A\n@%s\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1//push temp %s\n'%(index,segment_map[segment],index)
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
        asm_file.write(asm_code) 


def writeIf(command,label):
    if commandType(command) == 'C_IF':
        vmFileName = fileBaseName(asm_file)
        label = '%s.%s'%(vmFileName,label)
        asm_code = '@SP\nM=M-1\nD=M\n@%s\nD;JNE//if-goto %s\n'%(label,label)
        asm_file.write(asm_code) 
        

def close():
    asm_file.close() 


def writeHeadBlock():
    asm_file.write('//This File is generate by translator.\n//Implements by gongqingkui at 126.com\n\n')
