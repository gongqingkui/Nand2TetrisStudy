with open("Main.jack") as f:
    lines = f.readlines()

    for l in lines:
        i,j = 0,1
        while j <= len(l):
            if l[i] == '/':
                status = 'DIV_COMM_BEG'
                if l[j] == '/':
                    status = 'COMM_BEG'
                elif status == 'COMM_BEG' and l[j] == '*':
                    status = 'COMM2_WAI'
                elif status == 'COMM2_WAI' and l[j] == '*':
                    status = 'COMM2_BEG' 
                else:
                    status = 'DIV_BEG'
            j = j + 1
        print(line,end = "")
