#Program Demonstrating a Decorator That Performs Safe Division (Checks for Division by Zero)

def smart_divide(fn):
    def inner(a,b):
        print(f"i am going to divide {a} by {b}")
        if b == 0:
            print("cannot divide by zero ")
            return 
        fn(a,b)

    return inner

@ smart_divide
def divide(a,b):
    print(f"result of {a/b} :")
    
divide(10,0)
