#    Program to Find the Maximum Number Using reduce()
from functools import reduce
A = [int(x) for x in input("enter input :").split(",")]
max = reduce(lambda x,y : x if x>y else y,A)
print(max)
