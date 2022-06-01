# This file is implements of 'The elements of computer systems'
# chap 7.Virtual Machine:Stack 
# VM command parser module
# author:gongqingkui AT 126.com
# date:2022-05-12


def parser(asm=None):
    with open(asm, 'r', encoding='gb2312') as f:
        commandBuffer = f.readlines()
    return commandBuffer


def hasMoreCommand(commandBuffer):
    return bool(len(commandBuffer))


def advance(commandBuffer): 
    c = commandBuffer[0]
    del commandBuffer[0]
    return c.strip().lower().replace('\t',' ')


def commandType(command):
    if command == '':
        return 'BLANKLINE'
    elif command.startswith('\\'):
        return 'COMMENT'
    c = command.split(' ')
    return 'C_ARITHMETIC' if c[0] in ['add','sub','neg','eq','lt','gt','and','or','not']\
        else 'C_PUSH' if c[0] == 'push'\
        else 'C_POP' if c[0] == 'pop'\
        else 'C_LABEL' if c[0] == 'label'\
        else 'C_GOTO' if c[0] == 'goto'\
        else 'C_IF' if c[0] == 'if-goto'\
        else 'C_FUNCTION' if c[0] == 'function'\
        else 'C_RETURN' if c[0] == 'return'\
        else 'C_CALL' if c[0] == 'call' \
        else 'ERROR VM CODE %s'%command 


def arg1(command):
    c = command.split(' ')
    if commandType(command) == 'C_ARITHMETIC':
        return c[0] 
    elif commandType(command) == 'C_RETURN' or len(c)<=1: 
        return None
    else:
        return c[1]


def arg2(command):
    c = command.split(' ')
    if commandType(command) in ['C_PUSH','C_POP','C_FUNCTION','C_CALL']:
        return int(c[2])
    else:
        return None


if __name__ == '__main__':
    commandBuffer = openVMFile('SimpleAdd.vm')
    while hasMoreCommand(commandBuffer):
        c = advance(commandBuffer)
        print('%20s%10s%10s%10s' %
              (c, commandType(c), arg1(c),arg2(c)))
