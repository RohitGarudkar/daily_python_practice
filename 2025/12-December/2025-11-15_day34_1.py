#Raising exceptions

try:
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    if b == 0:
        raise ZeroDivisionError("'b' cannot be zero")
    else:
        print("I am in else bock")
        print(f"Result of Division = {a/b}")
except ZeroDivisionError as e:
    print("Cannot divide by Zero..")
    print(e)
