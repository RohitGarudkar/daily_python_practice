    #if 
     
num = int(input("Enter number between 1 to 5 :"))
if( num == 1):
    print("number is 1")
if( num == 2):
    print("number is 2")
if( num == 3):
    print("number is 3")
if( num == 4):
    print("number is 4")
if( num == 5):
    print("number is 5")

    #if - else

age = int(input("Enter your age :"))
if(age >= 18):
    print("can drive")
    print("can vote ")
else:
    print("can not drive ")
    print("can not vote")

    #if - elif - else

color = input("Enter color : ")
if( color == "red"):
    print("stop")
elif(color == "yellow"):
    print("look for ")
elif(color == "green" ):
    print("go")
else:
    print("light is broken")
