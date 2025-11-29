#Program Demonstrating Function Decorator to Add Extra Behavior Before and After a Function
def my_decorator(fn):
    def inner():
        print("Good Morning...")
        fn()
        print("How are you ?")
    return inner

@my_decorator
def greet():
    name = input("Enter your Name : ")
    print(f"hello {name}")

greet()
