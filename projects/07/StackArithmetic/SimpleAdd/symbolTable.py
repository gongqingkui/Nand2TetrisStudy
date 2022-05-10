# This file is implements of 'The elements of computer systesm'
# chap 6.Assembler
# author:gongqingkui AT 126.com
# date:2022-01-12
st ={}

def constructor():
    addEntry("R0",0)
    addEntry("R1",1)
    addEntry("R2",2)
    addEntry("R3",3)
    addEntry("R4",4)
    addEntry("R5",5)
    addEntry("R6",6)
    addEntry("R7",7)
    addEntry("R8",8)
    addEntry("R9",9)
    addEntry("R10",10)
    addEntry("R11",11)
    addEntry("R12",12)
    addEntry("R13",13)
    addEntry("R14",14)
    addEntry("R15",15)
    addEntry("SP",0)
    addEntry("LCL",1)
    addEntry("ARG",2)
    addEntry("THIS",3)
    addEntry("THAT",4)
    addEntry("SCREEN",0x4000)
    addEntry("KBD",0x6000)
    return st

def addEntry(symbol,address):
    st[symbol]=address

def contains(symbol):
    return symbol in st 

def getAddress(symbol):
    return st.get(symbol,None)

constructor()

if __name__ == '__main__':
    if contains("RO"):
        print("RO",getAddress("RO"))
