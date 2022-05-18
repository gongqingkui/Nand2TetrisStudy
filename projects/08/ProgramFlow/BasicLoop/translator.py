from parserVMTranslator import parser,hasMoreCommand,advance,commandType,arg1,arg2
from codeWriter import asm_file,CodeWriter,writeArithmetic,writePushPop,close,writeHeadBlock,writeLabel,writeGoto,writeIf
import os
import sys

def vm2asm(file_): 
    commands = parser(file_)
    while hasMoreCommand(commands):
        c = advance(commands)
        #print('%20s%10s%10s%10s' % (c, commandType(c), arg1(c),arg2(c)))
        writeArithmetic(c)
        writePushPop(c,arg1(c),arg2(c))
        writeLabel(c,arg1(c))
        writeGoto(c,arg1(c))
        writeIf(c,arg1(c))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('input file or dir:')
    elif os.path.exists(sys.argv[1]):
        #process of single file
        if os.path.isfile(sys.argv[1]):
            file_ = sys.argv[1]
            CodeWriter(file_[:-2]+'asm') 
            writeHeadBlock() 
            vm2asm(file_)
            close()
        #process of dir
        elif os.path.isdir(sys.argv[1]):
            dir_ = sys.argv[1]
            for root,sub,files_ in os.walk(dir_):
                CodeWriter(os.path.join(dir_,os.path.dirname(dir_)+'.asm'))
                writeHeadBlock() 
                for file_ in files_: 
                    if file_.endswith('.vm'):
                        file_ = os.path.join(root,file_)
                        #print(os.path.exists(file_))
                        vm2asm(file_)
                close()
