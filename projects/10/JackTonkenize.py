# This file is implements of 'The elements of computer systems'
# chap 10.compiler
# Tokenize module
# author:gongqingkui AT 126.com
# date:2023-07-09

def parser(code=None): 
    with open(code, 'r', encoding='gb2312') as f:
        JackCodeBuffer = f.readlines()
    return JackCodeBuffer 


def hasMoreCommand(JackCodeBuffer):
    return bool(len(JackCodeBuffer))


def advance(JackCodeBuffer): 
    c = JackCodeBuffer[0]
    del JackCodeBuffer[0]
    return c.strip().lower()#.replace(' ','')


def JackCodeType(JackCode):
    if JackCode == '':
        return 'BLANKLINE'
    elif JackCode.startswith('//'):
        return 'COMMENT'
    # coding.............TODO 
    c = JackCode.split(' ')
    return 'C_ARITHMETIC' if c[0] in ['add','sub','neg','eq','lt','gt','and','or','not']\
        else 'C_PUSH' if c[0] == 'push'\
        else 'C_POP' if c[0] == 'pop'\
        else 'C_LABEL' if c[0] == 'label'\
        else 'C_GOTO' if c[0] == 'goto'\
        else 'C_IF' if c[0] == 'if-goto'\
        else 'C_FUNCTION' if c[0] == 'function'\
        else 'C_RETURN' if c[0] == 'return'\
        else 'C_CALL' if c[0] == 'call' \
        else 'ERROR VM CODE %s'%JackCode 


if __name__ == '__main__':
    JackCodeBuffer = parser('ArrayTest/main.jack') 
    print(JackCodeBuffer)
    while hasMoreCommand(JackCodeBuffer):
        c = advance(JackCodeBuffer)
        print('%20s%10s' % (c, JackCodeType(c)))
