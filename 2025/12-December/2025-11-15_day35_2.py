#Custome Exception

class MyError(Exception):
    
    #constroctor 
    def __init__(self,value):
        self.value = value

    #__str__ is to print the value
    def __str__(self):
        return(repr(self.value)) 
try:
    x = int(input("Enter a number upto 100 "))
    if x>100:
        raise MyError(x)
    else:
        print(f"{x} is valid number ")
except MyError as e:
    print(f"Exception occured :Invalid Number : {e}")
    
