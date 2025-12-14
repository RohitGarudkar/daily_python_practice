
#Exception Handling try...finally block

try:
    fp = open("test.txt","r")
    try:
        fp.write("HI I am good")
    finally:
        fp.close()
        print("file closed...")
except Exception as e :
    print("file mode error ")
    print(e)

print("I am in other part")
