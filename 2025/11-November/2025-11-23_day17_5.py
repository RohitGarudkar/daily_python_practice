#even list using filter and lambda
#A = [int(i) for i in input("Enter numer seperated by ',' :").split(",")]
A = [i for i in range(1,11)]
evenlist = list(filter(lambda x : x%2 == 0, A))
print(evenlist)
