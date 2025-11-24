#     Program to Calculate the Sum of Squares of First 10 Natural Numbers Using reduce()

from functools import reduce
A = [int(x) for x in range(1,11)]
square_num = reduce(lambda x,y : x+(y*y) ,A)
print(square_num)
