#Program Using a Decorator to Convert a Returned Name to Uppercase
def my_decorator(fn):
    def inner():
        upper = fn()
        up = upper.upper()
        print(f"your name is {up}") 
    return inner    


@ my_decorator
def small_case():
    name = input("Enter your Name : ")
    return name
small_case()
