#      Program to Find the Sum of First 10 Natural Numbers Using reduce()
from functools import reduce
A = [int(x) for x in range(1,11)]
sum = reduce(lambda x,y : x+y ,A)
print(sum)
