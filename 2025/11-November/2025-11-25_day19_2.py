#   Program to Find the Minimum Number Using reduce()

from functools import reduce
A = [int(x) for x in input("enter input :").split(",")]
min = reduce(lambda x, y: x if x < y else y, A)
print(min)
