with open("one.txt", "r") as f:
    while (True):
        line = f.readline()
        if (line == ""):
            break

        else:
            #print(line,end="")

            t1=line[0]
            if t1=="t" or t1=="T":
                continue
            else:
                print(line,end="")