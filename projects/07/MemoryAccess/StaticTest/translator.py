from parserVMTranslator import parser,hasMoreCommand,advance,commandType,arg1,arg2
from codeWriter import f,CodeWriter,writeArithmetic,writePushPop,close,writeHeadBlock
import os
import sys

def vm2asm(file_): 
    commands = parser(file_)
    while hasMoreCommand(commands):
        c = advance(commands)
        #print('%20s%10s%10s%10s' % (c, commandType(c), arg1(c),arg2(c)))
        writeArithmetic(c)
        writePushPop(c,arg1(c),arg2(c))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('input file or dir:')
    elif os.path.exists(sys.argv[1]):
        if os.path.isfile(sys.argv[1]):
            file_ = sys.argv[1]
            CodeWriter(file_[:-2]+'asm') 
            writeHeadBlock() 
            vm2asm(file_)
            close()
        elif os.path.isdir(sys.argv[1]):
            dir_ = sys.argv[1]
            for root,sub,files_ in os.walk(dir_):
                CodeWriter(dir_+'.asm') 
                writeHeadBlock() 
                for file_ in files_: 
                    if file_.endswith('.vm'):
                        file_ = os.path.join(root,file_)
                        #print(os.path.exists(file_))
                        vm2asm(file_)
                close()
