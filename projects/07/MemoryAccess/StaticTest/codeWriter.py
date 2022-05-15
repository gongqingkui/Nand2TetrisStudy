# This file is implements of 'The elements of computer systems'
# chap 7.Virtual Machine:Stack
# CodeWrite module
# author:gongqingkui AT 126.com
# date:2022-05-12

from parserVMTranslator import commandType,arg2

f = None
jmp_index = 0
segment_map = {'local':'LCL','argument':'ARG','this':'THIS','that':'THAT','temp':'R5','pointer':'R3','static':'16'}

def CodeWriter(file_):
    global f
    f = open(file_,'w')
    return f

    
def writeArithmetic(command):
    global jmp_index
    c = command.split(' ')
    if commandType(command) == 'C_ARITHMETIC':
        if c[0] in ['add','sub','and','or']:
            to = '//Arithmetic\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M%sD'
            oper = ''
            if c[0] == 'add':
                oper = '+'
            elif c[0] == 'sub':
                oper = '-'
            elif c[0] == 'and':
                oper = '&'
            elif c[0] == 'or':
                oper = '|'
            to = to%oper 
        if c[0] in ['eq','lt','gt']:
            to = '//comparse\n@SP\nAM=M-1\nD=M\nA=A-1\nMD=M-D\n@TRUE_%s\nD;%s\n@SP\nD=A\n@0\nA=M-1\nM=D\n@CONTINUE_%s\nD;JMP\n(TRUE_%s)\n@1\nD=-A\n@SP\nA=M-1\nM=D\n(CONTINUE_%s)'
            oper = ''
            if c[0] == 'eq':
                oper = 'JEQ'
            elif c[0] == 'lt':
                oper = 'JLT'
            elif c[0] == 'gt':
                oper = 'JGT'
            elif c[0] == 'or':
                oper = '|'
            to = to%(jmp_index,oper,jmp_index,jmp_index,jmp_index) 
            jmp_index += 1
        elif c[0] in ['neg','not']:
            to = '//single element - !\n@SP\nA=M-1\nM=%sM'
            oper = ''
            if c[0] == 'neg':
                oper = '-'
            elif c[0] == 'not':
                oper = '!'
            to = to%oper 
        f.write(to+'\n')


def writePushPop(command,segment,index):
    print(command,segment,index)
    if commandType(command) == 'C_PUSH':
        if segment == 'constant':
            to = '//push constant\n@%s\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'%index
        if segment in ['temp','static']:
            to = '//push temp\n@%s\nD=A\n@%s\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'%(index,segment_map[segment])
        if segment == 'pointer':
            to = '//push pointer\n@%s\nD=A\n@%s\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'%(index,segment_map[segment])
        if segment in ['local','argument','this','that']:
            to = '//push\n@%s\nD=A\n@%s\nA=M\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'%(index,segment_map[segment])
        f.write(to)
    if commandType(command) == 'C_POP':
        if segment in ['temp','static']:
        #if segment == 'temp':
            to = '//pop temp\n@%s\nD=A\n@%s\nD=A+D\n@add\nM=D\n@SP\nAM=M-1\nD=M\n@add\nA=M\nM=D\n'%(index,segment_map[segment]) 
        if segment == 'pointer':
            to = '//pop pointer\n@%s\nD=A\n@%s\nD=A+D\n@add\nM=D\n@SP\nAM=M-1\nD=M\n@add\nA=M\nM=D\n'%(index,segment_map[segment]) 
        if segment in ['local','argument','this','that']:
            to = '//pop\n@%s\nD=A\n@%s\nA=M\nD=A+D\n@add\nM=D\n@SP\nAM=M-1\nD=M\n@add\nA=M\nM=D\n'%(index,segment_map[segment]) 
        f.write(to) 


def close():
    f.close() 


def writeHeadBlock():
    #f.write('@true\nM=-1\n@false\nM=0'+'\n')
    f.write('//This File is generate by translator.\n//Implements by gongqingkui at 126.com\n\n')
