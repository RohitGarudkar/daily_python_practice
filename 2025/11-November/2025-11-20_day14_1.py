# star patter using for loop 

n = int(input("enter number to ger the matrix : "))

for i in range (n+1):
    for j in range (i):
        print("*", end=" ")
    print()
    

for i in range (n-1,0,-1):
    for j in range (i):
        print("*" , end=" ")
    print()

#output

'''

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

'''
