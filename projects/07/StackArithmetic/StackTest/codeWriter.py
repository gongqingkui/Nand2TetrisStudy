# This file is implements of 'The elements of computer systems'
# chap 7.Virtual Machine:Stack
# CodeWrite module
# author:gongqingkui AT 126.com
# date:2022-05-12

from parserVMTranslator import commandType,arg2

f = None
jmp_index = 0

def CodeWriter(file_):
    global f
    f = open(file_,'w')
    return f

    
def writeArithmetic(command):
    global jmp_index
    c = command.split(' ')
    if commandType(command) == 'C_ARITHMETIC':
        if c[0] in ['add','sub','and','or']:
            to = '@SP\nAM=M-1\nD=M\nA=A-1\nM=M%sD'
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
            to = '@SP\nAM=M-1\nD=M\nA=A-1\nMD=M-D\n@TRUE_%s\nD;%s\n@SP\nD=A\n@0\nA=M-1\nM=D\n@CONTINUE_%s\nD;JMP\n(TRUE_%s)\n@1\nD=-A\n@SP\nA=M-1\nM=D\n(CONTINUE_%s)'
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
            to = '@SP\nA=M-1\nM=%sM'
            oper = ''
            if c[0] == 'neg':
                oper = '-'
            elif c[0] == 'not':
                oper = '!'
            to = to%oper 
        f.write(to+'\n')


def writePushPop(command,segment,index):
    if commandType(command) == 'C_PUSH' and segment == 'constant':
        to = '@%s\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'%index
        f.write(to)


def close():
    f.close() 


def writeHeadBlock():
    #f.write('@true\nM=-1\n@false\nM=0'+'\n')
    f.write('//This File is generate by translator.\n\n')
