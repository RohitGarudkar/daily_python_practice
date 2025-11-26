#Demonstration of Generator and yield in Python

def my_gen():
    print("First Item")
    yield 10
    print("Second Item")
    yield 20
    print("Third Item")
    yield 30
    print("Fourth Item")
    yield 40
gen = my_gen()

while True:
    try:
        print(next(gen))
    except StopIteration: break
