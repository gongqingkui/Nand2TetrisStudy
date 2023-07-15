# washing the jack file
import re

JackCodeBuffer = ""

with open('Main.jack') as f:
    lines = f.readlines() 
    for line in lines:
        #print(re.findall(r'\/[\/*].*$',line))
        JackCodeBuffer += re.sub(r'\/[\/*].*$','',line.strip())
    print(JackCodeBuffer)
    #print(re.split(r'\W',JackCodeBuffer))
