# Declaring Multiple Exceptions
try: 
    a = 10
    b = 'p'
    c = a/b
except (ArithmeticError) as e:
    print(e)
except (IOError) as e:
    print(e)
except (TypeError) as e:
    print(e)
except (NameError) as e:
    print(e)
except (ZeroDivisionError) as e:
    print(e)
except (IntendationError) as e: 
    print(e)
else: 
    print("I am in Else part")
