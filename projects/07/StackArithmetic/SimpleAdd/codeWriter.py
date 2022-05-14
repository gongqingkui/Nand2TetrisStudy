# This file is implements of 'The elements of computer systems'
# chap 7.Virtual Machine:Stack
# CodeWrite module
# author:gongqingkui AT 126.com
# date:2022-05-12

from parserVMTranslator import commandType,arg2

f = None

def CodeWriter(file_):
    global f
    f = open(file_,'w')
    return f

    
def writeArithmetic(command):
    c = command.split(' ')
    if commandType(command) == 'C_ARITHMETIC':
        if c[0] in ['add','sub','and','or']:
            to = '@SP\nAM=M-1\nD=M\nA=A-1\nM=D%sM'
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
        elif c[0] in ['neg','not']:
            to = '@SP\nA=M-1\nM=%M'
            oper = ''
            if c[0] == 'neg':
                oper = '-'
            elif c[0] == 'not':
                oper = '!'
            to = to%oper 
        f.write(to+'\n')


def writePushPop(command,segment,index):
    if commandType(command) == 'C_PUSH' and segment == 'constant':
        to = '@%s\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1'%index
        f.write(to+'\n')


def close():
    f.close() 
