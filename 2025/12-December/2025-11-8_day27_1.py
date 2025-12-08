#file handeling in python

fp = open("test.txt","r")
while True:
    line = next(fp)
    print(line)
fp.close()
