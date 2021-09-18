from parserAssembler import openAsmFile,hasMoreCommand,advance,commandType,symbol,dest,comp,jump
from codeAssembler import destCode,compCode,jumpCode

if __name__ == '__main__':
    asmFile = 'max/MaxL.asm'
    hackFile = asmFile[:-3] + 'hack'
    hackFile = open(hackFile,'w',encoding='ANSI')

    commandBuffer = openAsmFile('max/MaxL.asm')
    while hasMoreCommand(commandBuffer):
        c= advance(commandBuffer)
        to = '%20s%10s%10s%10s%10s%10s'%(c,commandType(c),symbol(c),dest(c),comp(c),jump(c))
        print(to)
        if commandType(c) in ['A_COMMAND','L_COMMAND']:
            to = '%16s\n'%(bin(int(symbol(c)))[2:].zfill(16))
            print(to)
            hackFile.write(to)
        elif commandType(c) in ['C_COMMAND']:
            print('%20s%10s%10s%10s'%(c,dest(c),comp(c),jump(c)))
            to = '111%7s%3s%3s\n'%(compCode(comp(c)),destCode(dest(c)),jumpCode(jump(c)))
            print(to)
            hackFile.write(to)
     
    hackFile.close()
