
        #fibonaccci

num = int(input("Enter number : "))
a,b = 0,1

if num == 0:
    print("The given number is 0 ")
elif num == 1:
    print("The given number is 1")
else:
    print("Fibonacci")
    for i in range (num):
        print(a)
        a,b = b,a+b
        
