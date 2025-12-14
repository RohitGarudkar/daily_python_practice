#else and finally
try:
    print("in -> try block ")
    x = int(input("Enter value of x : "))
    y = int(input("Enter value of y : "))
    z = x/y

except ZeroDivisionError as ze:
    print("In -> ZeroDivision block")
    print("Dicision by 0 is not accept")
    print(ze)
except ValueError as ve:
    print("ValueError Block")
    print(ve)
else:
    print("In -> else block")
    print(f"Division = {z}")
finally:
    print("In -> finally block")
    x = 0
    y = 0
    print(f"x = {x} and y = {y}")
print("now i am->  out of try except and else and finally")
