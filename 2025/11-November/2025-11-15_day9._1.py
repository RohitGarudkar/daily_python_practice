#nested if 

age = int(input("Enter age : "))
if (age >= 18 ):
    if(age >= 80):
        print("you can not drive")
    else:
        print("you can drive")
else:
    print("you can not drive")
