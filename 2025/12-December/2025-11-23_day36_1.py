class InvalidAge(Exception):
    
    #constroctor
    def __init__(self,age):
        self.age = age

    #__str__ is to print the value
    def __str__(self):
        return(repr(self.age))
try:
    age = int(input("Ente age :"))
    if age < 18:
        raise InvalidAge(age)
    else: 
        print(f"{age} is valid")
except InvalidAge as e:
    print(f"Exception occured : Invalid AGE : {age}")
