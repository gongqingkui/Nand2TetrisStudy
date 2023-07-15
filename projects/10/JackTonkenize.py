# This file is implements of 'The elements of computer systems'
# chap 10.compiler
# Tokenize module
# author:gongqingkui AT 126.com
# date:2023-07-09
import re

JackCodeBuffer = ""

keywords = ['class','constructor','function',
            'method','field','static','var',
            'int','char','boolean','void','true',
            'false','null','this','let','do',
            'if','else','while','return']

symbols = "{}[]().,;+-*/&|<>=~" 

def parser(code=None): 
    with open(code, 'r', encoding='gb2312') as f:
        JackCodeBuffer = f.readlines()
    JackCodeBuffer = "".join(JackCodeBuffer)
    JackCodeBuffer = re.sub(r'\/[\/*].*','',JackCodeBuffer).replace('\n','').strip()
    return JackCodeBuffer 


def hasMoreTokens(JackCodeBuffer):
    return bool(len(JackCodeBuffer))


def advance(JackCodeBuffer): 
    for kw in keywords:
        if JackCodeBuffer.find(kw) == 0:
            return kw 
    for sb in symbols:
        if JackCodeBuffer.find(sb) == 0:
            return sb 
    if JackCodeBuffer[0] == '"':
        stringConstant = JackCodeBuffer[0:JackCodeBuffer.find('"',1)]
        return stringConstant
    elif re.match(r'\d',JackCodeBuffer):
        integertConstant = re.match(r'\d',JackCodeBuffer).group(0)
        return integertConstant 
    else:
        identifier = JackCodeBuffer[0:JackCodeBuffer.find(' ')+1]
        if identifier.find('('):
            identifier = identifier[0:identifier.find('(')]
        elif identifier.find(';'):
           identifier = identifier[0:identifier.find(';')]
        elif identifier.find(','):
           identifier = identifier[0:identifier.find(',')]
        elif identifier.find('.'):
           identifier = identifier[0:identifier.find('.')]
        else:
            return identifier
        return identifier


def tokenType(JackCode):
    if JackCode == '':
        return 'BLANKLINE'
    return 'KEYWORD' if JackCode in keywords\
        else 'SYMBOL' if JackCode in symbols\
        else 'STRING_CONST' if JackCode[0] == '"'\
        else 'INT_CONST' if JackCode[0] in '0123456789'\
        else 'IDENTIFIER' 


if __name__ == '__main__':
    JackCodeBuffer = parser('ArrayTest/main.jack') 
    while hasMoreTokens(JackCodeBuffer):
        c = advance(JackCodeBuffer)
        JackCodeBuffer = JackCodeBuffer[len(c):].strip()
        print('%20s%10s' % (c, tokenType(c)))
