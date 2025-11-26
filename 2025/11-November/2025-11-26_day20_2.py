#Multiplication Table Generator Using yield in Python

def Table(num):
    for i in range(1,11):
        yield f"{num} * {i} = {num*i}"

n =int(input("enter any number : "))
print(f"Table of {n}")

table = Table(n)

for i in table :
    print(i)
