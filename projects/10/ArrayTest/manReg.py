import string

with open('Main.jack') as f:
    contents = f.readlines()
    contents = ''.join(contents)

print(contents)

i = 0

def getChar():
    global i
    if i < len(contents): 
        c = contents[i]
        i = i + 1
        return c
    else:
        return None

def unGetChar():
    global i
    i = i - 1

tk = []
c = getChar()
while c != None:
    if c.isdigit(): 
        tk.append(c)
        c = getChar()
        while c.isdigit():
            tk.append(c)
            c = getChar()
        print("NUM",''.join(tk))
        unGetChar()
        tk = []
    elif c.isalpha():
        tk.append(c)
        c = getChar()
        while c.isalpha():
            tk.append(c)
            c = getChar()
        print("LETTER",''.join(tk))
        unGetChar()
        tk = []
    elif c in "[]{}().;,=<+":
        tk.append(c)
        print("OPER",''.join(tk))
        tk = []
    elif c == '"':
        tk.append(c)
        c = getChar()
        while c != '"':
            tk.append(c)
            c = getChar()
        tk.append('"')
        print("STRING",''.join(tk))
        #unGetChar()
        tk = []
    elif c == '/':
        tk.append(c)
        c = getChar()
        if c not in ['/','*']:
            print("OPER /:",''.join(tk))
            tk = []
        elif c in ['/','*']:
            tk.append(c)
            c = getChar()
            while c not in ['\r\n','\r','\n']:
                tk.append(c)
                c = getChar()
            print("COMMENT:",''.join(tk))
            unGetChar()
            tk = [] 
    c = getChar()
