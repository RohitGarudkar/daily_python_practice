#filter function 

A = [int(i) for i in input("Enter numer seperated by ',' :").split(",")]
evenlist = list(filter(lambda x : x%2 == 0, A))
print(evenlist)
