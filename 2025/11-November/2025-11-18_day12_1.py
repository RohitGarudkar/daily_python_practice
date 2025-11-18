
        #factorial

num = int(input("Enter number : "))
fact = 1

if num == 0 or num == 1:
    print("factorial is negative value or 1")
else:
    for i in range(1, num+1):
        fact *= i
    print(f"the factorial of {num} is {fact}" )
