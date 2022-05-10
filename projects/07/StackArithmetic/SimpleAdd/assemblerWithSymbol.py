# This file is implements of 'The elements of computer systesm'
# chap 6.Assembler
# author:gongqingkui AT 126.com
# date:2021-09-18

import sys
from parserAssembler import openAsmFile, hasMoreCommand, advance, commandType, symbol, dest, comp, jump
from codeAssembler import destCode, compCode, jumpCode
from symbolTable import st,addEntry,contains,getAddress

if __name__ == '__main__':
    if sys.argv[1]:
        asmFile = sys.argv[1]
    else:    
        asmFile = 'max/MaxL.asm'
    hackFile = asmFile[:-3] + 'hack'
    hackFile = open(hackFile, 'w', encoding='ANSI')

    #step1.  
    commandBuffer = openAsmFile(asmFile)
    add = 0
    while hasMoreCommand(commandBuffer):
        c = advance(commandBuffer)
        if commandType(c) in ['A_COMMAND', 'C_COMMAND']:
            add+=1
        elif commandType(c) in ['L_COMMAND']:
            addEntry(symbol(c),add)
    commandBuffer.clear()
    print(st)

    #step2.
    commandBuffer = openAsmFile(asmFile)
    pc=16
    while hasMoreCommand(commandBuffer):
        c = advance(commandBuffer)
        to = '%10s%10s%10s%10s%10s%10s' % (
            c, commandType(c), symbol(c), dest(c), comp(c), jump(c))
        print(to,end='|')
        if commandType(c) == 'A_COMMAND':
            if symbol(c).isnumeric():
                add = symbol(c)
            else:
                if contains(symbol(c)):
                    add = getAddress(symbol(c))
                else:
                    addEntry(symbol(c),pc)
                    pc += 1
                    add = getAddress(symbol(c))
            to = '%16s\n' % (bin(int(add))[2:].zfill(16))
            print(to)
            hackFile.write(to)
        if commandType(c) == 'C_COMMAND':
            to = '111%7s%3s%3s\n' % (
                compCode(comp(c)), destCode(dest(c)), jumpCode(jump(c)))
            print(to)
            hackFile.write(to)
    hackFile.close()
