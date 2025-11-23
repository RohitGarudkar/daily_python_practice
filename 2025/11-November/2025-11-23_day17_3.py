# print table using lambda function
num = int(input("enter any number for table generation"))
table = list(map(lambda x: num*x,[i for i in range(1,11)]))
print(f"Table of {num}")
for i in range(len(table)):
    print(f"{num} * {i+1}  = {table[i]}")
