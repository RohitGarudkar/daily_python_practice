#odd list using fileter and lambda 
A = [int(i) for i in input("Enter numer seperated by ',' :").split(",")]
#A = [i for i in range(1,11)]
oddlist = list(filter(lambda x : x%2 != 0, A))
print(oddlist)
