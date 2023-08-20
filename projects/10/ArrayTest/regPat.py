import re

p = re.compile("(\/\/.*$)|(\/\*\*.*\*\/)|(\w+)|(\d+)|(\".*\")|([\.\{\}\[\]\(\);,=<\/\+])")
with open("Main.jack") as f:
    lines = f.readlines()

    for line in lines:
        print(line,end = "")
        it = p.finditer(line) 
        for m in it:
            if m.group(1):
                print("COMMENT",m.group(1))
            if m.group(2):
                print("COMMENT",m.group(2))
            if m.group(3):
                print("LITER",m.group(3))
            if m.group(4):
                print("DIGIT",m.group(4))
            if m.group(5):
                print("STRING",m.group(5))
            if m.group(6):
                print("OPER",m.group(6))
            #print(m.group(1),m.group(2),m.group(3),m.group(4),m.group(5))
