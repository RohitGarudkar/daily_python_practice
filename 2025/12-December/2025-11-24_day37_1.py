 #Handling Custom Errors Using Exception Class

class ErrorInCode(Exception):
    
    #constroctor
    def __init__(self,data):
        self.data = data

    #__str__ is to print the value
    def __str__(self):
        return(repr(self.data))
try:
    a = int(input("Enter value for A : "))
    b = int(input("Enter value for B : ")) 
    if a == b:
        raise ErrorInCode(505)
    else:
        print("No error in code")
except ErrorInCode as e:
    print(f"Exception occured : Received Error : {e}")
