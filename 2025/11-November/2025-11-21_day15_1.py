#                                    Decorator Function 

def my_decorator(fn):
    def inner():
        print("Good Morning...")
        fn()
        print("How are you ?")


@my_decorator
def greet():
    name = input("Enter your Name : ")
    print(f"hello {name}")
