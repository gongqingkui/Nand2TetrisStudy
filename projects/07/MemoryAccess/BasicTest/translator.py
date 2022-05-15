from parserVMTranslator import parser,hasMoreCommand,advance,commandType,arg1,arg2
from codeWriter import f,CodeWriter,writeArithmetic,writePushPop,close,writeHeadBlock


commands = parser('BasicTest.vm')
CodeWriter('BasicTest.asm')

writeHeadBlock()

while hasMoreCommand(commands):
    c = advance(commands)
    print('%20s%10s%10s%10s' %
          (c, commandType(c), arg1(c),arg2(c)))
    writeArithmetic(c)
    writePushPop(c,arg1(c),arg2(c))


close()
