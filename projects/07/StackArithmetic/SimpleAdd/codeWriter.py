# This file is implements of 'The elements of computer systems'
# chap 7.Virtual Machine:Stack
# CodeWrite module
# author:gongqingkui AT 126.com
# date:2022-05-12

f = None

def CodeWriter(file_):
    global f
    f = open(file_,'w')
    return f

    
def writeArithmetic(command):
    f.write(command)


def writePushPop(command,segment,index):
    f.write('%s%s%s'%(command,segment,index))


def close():
    f.close() 
