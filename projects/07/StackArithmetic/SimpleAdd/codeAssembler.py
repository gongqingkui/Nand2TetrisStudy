# This file is implements of 'The elements of computer systesm'
# chap 6.Assembler
# author:gongqingkui AT 126.com
# date:2021-09-18

jumpTable = {
    'null': '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111'}

compTable = {
    # a = 0 oper with A
    '0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100',
    'A': '0110000', '!D': '0001101', '!A': '0110001', '-D': '0001111',
    '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110',
    'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D': '0000111',
    'D&A': '0000000', 'D|A': '0010101',

    # a = 1 oper with M
    'M': '1110000',  '!M': '1110001', '-M': '1110011', 'M+1': '1110111',
    'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111',
    'D&M': '1000000', 'D|M': '1010101',
}


def destCode(amd=None):
    return '%s%s%s' % ('1' if 'A' in amd else '0',
                       '1' if 'D' in amd else '0',
                       '1' if 'M' in amd else '0')


def compCode(c=None):
    return compTable[c]


def jumpCode(j=None):
    return jumpTable[j]


if __name__ == '__main__':
    # D=M+A
    print(destCode('D'), compCode('D-1'), jumpCode('null'))
    # D;JLE
    print(destCode('null'), compCode('D'), jumpCode('JLE'))
