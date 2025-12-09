import os 
try:
    fp = open("test.txt","r")
except Exception as e:
    print("----------")
    print(e)
else:
    print("The file open successfully")
    os.startfile("test.txt")
    fp.close()
