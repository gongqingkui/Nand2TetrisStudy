# This file is implements of 'The elements of computer systems'
# chap 6.Assembler
# author:gongqingkui AT 126.com
# date:2021-09-18

def openAsmFile(asm=None):
    with open(asm, 'r', encoding='ANSI') as f:
        commandBuffer = f.readlines()
    return commandBuffer


def hasMoreCommand(commandBuffer):
    return bool(len(commandBuffer))


def advance(commandBuffer):
    c = commandBuffer[0]
    if c.find('/'):
        c = c[:c.find('/')]
    del commandBuffer[0]
    return c.strip().replace(' ','')


def commandType(command):
    c = command
    return 'A_COMMAND' if c.startswith('@')\
        else 'L_COMMAND' if c.startswith('(')\
        else 'COMMENT' if c.startswith('/')\
        else 'BLANKLINE' if c == ''\
        else 'C_COMMAND'


def symbol(command):
    if commandType(command) in ['A_COMMAND', 'L_COMMAND']:
        return command.replace('@', '').replace('(', '').replace(')', '')
    return None


def dest(command):
    if commandType(command) in ['C_COMMAND']:
        if command.find('=') != -1:
            return command[0:command.find('=')]
        else:
            return 'null'
    return None


def comp(command):
    if commandType(command) in ['C_COMMAND']:
        if command.find('=') != -1:
            return command[command.find('=')+1:]
        elif command.find(';') != -1:
            return command[0:command.find(';')]
        else:
            return 'null'
    return None


def jump(command):
    if commandType(command) in ['C_COMMAND']:
        if command.find(';') != -1:
            return command[command.find(';')+1:]
        else:
            return 'null'
    return None


if __name__ == '__main__':
    commandBuffer = openAsmFile('add/Add.asm')
    commandBuffer = openAsmFile('max/Max.asm')
    commandBuffer = openAsmFile('pong/pong.asm')
    while hasMoreCommand(commandBuffer):
        c = advance(commandBuffer)
        print('%20s%10s%10s%10s%10s%10s' %
              (c, commandType(c), symbol(c), dest(c), comp(c), jump(c)))
