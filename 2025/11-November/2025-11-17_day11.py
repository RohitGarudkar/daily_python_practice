#palindrom

a = int(input("Enter number :"))
s = str(a)

if s == s[::-1]:
    print("the given number is palindrom")
else:
    print("the given number is not palindrom")
