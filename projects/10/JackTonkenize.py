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
i,j = 0,1
lineno,colno = 0,0

def parser(code=None): 
    with open(code, 'r', encoding='gb2312') as f:
        JackCodeBuffer = f.readlines()
    #JackCodeBuffer = "".join(JackCodeBuffer)
    #JackCodeBuffer = re.sub(r'\/[\/*].*','',JackCodeBuffer).replace('\n','').strip()
    #JackCodeBuffer = re.sub(r'([\(\)\[\]\{\}\.,;\+\-\*\/\&\|<>=~])',r' \1 ',JackCodeBuffer)
    #print(JackCodeBuffer)
    return JackCodeBuffer 


def hasMoreTokens(JackCodeBuffer):
    #return bool(len(JackCodeBuffer))
    return not(len(JackCodeBuffer) - lineno) or (len(JackCodeBuffer[-1]) - j)

def advance2(JackCodeBuffer): 
    global i,j,lineno,colno
    status = ""
    if JackCodeBuffer[i] == '/':
        if JackCodeBuffer[j] == '/':
            j = JackCodeBuffer.index('\n',i)
            lineno +=1 
            print(f"COMMENT{lineno},{colno} {i}:{j}:{JackCodeBuffer[i:j]}")
            
        if JackCodeBuffer[j] == '*' and JackCodeBuffer[j+1] == '*':
            j = JackCodeBuffer.index('*/',i)
            lineno +=1 
            print(f"COMMENT{lineno},{colno} {i}:{j}:{JackCodeBuffer[i:j]}")
    if JackCodeBuffer[i] == '\n':
        lineno += 1
        print(f"BLANK_LINE")
    i = j + 1
    j = i + 1

def advance(JackCodeBuffer): 
    global i,j,lineno,colno
    for lineno,line in enumerate(JackCodeBuffer):
        if re.match(r'^\/\/.*$',line) or re.match(r'^\/\*{2}.*\*\/$',line):
            print(f'line {lineno} type:comment:{line}') 
        if re.match(r'^$',line):
            print(f'line {lineno} type:Blank') 
        while i < len(line):
            m = re.search(r'[a-zA-Z0-9]*',line[i:])
            if m: 
                tok = m.group(0)
                if tok in keywords:
                    print(f'line {lineno} type:keyword:{tok}') 
                else:
                    print(f'line {lineno} type:identifier:{tok}') 


        
  
        
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
    print(JackCodeBuffer)

    c = advance(JackCodeBuffer)
    print('%20s%10s' % (c, tokenType(c)))
    c = advance(JackCodeBuffer)
    print('%20s%10s' % (c, tokenType(c)))
    c = advance(JackCodeBuffer)
    print('%20s%10s' % (c, tokenType(c)))
    c = advance(JackCodeBuffer)
    print('%20s%10s' % (c, tokenType(c)))
    c = advance(JackCodeBuffer)
    print('%20s%10s' % (c, tokenType(c)))
    c = advance(JackCodeBuffer)
    print('%20s%10s' % (c, tokenType(c)))
    c = advance(JackCodeBuffer)
    print('%20s%10s' % (c, tokenType(c)))
    c = advance(JackCodeBuffer)
    print('%20s%10s' % (c, tokenType(c)))
    c = advance(JackCodeBuffer)
    print('%20s%10s' % (c, tokenType(c)))
    #while hasMoreTokens(JackCodeBuffer):
    #    c = advance(JackCodeBuffer)
        #JackCodeBuffer = JackCodeBuffer[len(c):].strip()
    #     print('%20s%10s' % (c, tokenType(c)))
