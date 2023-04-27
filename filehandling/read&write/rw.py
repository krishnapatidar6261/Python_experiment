with open("wr.txt","w+") as f:
    f.write("heloo")
    f.write("\n i like app")
    f.seek(0)
    print(f.read())
    f.seek(5)
    print(f.read())
