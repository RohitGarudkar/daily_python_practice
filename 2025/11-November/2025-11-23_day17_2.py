#smart divide

def my_decorator(fn):
    def inner(s):
        big_str = s.upper()
        print(f"your name is {big_str}") 
    return inner    


@ my_decorator
def small_case():
    pass
name = input("Enter your Name : ")    
small_case(name)
