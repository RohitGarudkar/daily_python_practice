#Declaring Multiple Exceptions
try:
    a = 10
    b = 'p'
    c = a/b
except (ArithmeticError,IOError,TypeError,NameError) as e:
    print("Arithmetic Exception")
    print(e)
else:
    print("Result of Division : {c}")
    print("Successfully Done... Else part")
