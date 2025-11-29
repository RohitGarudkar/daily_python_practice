#Program to Identify Odd and Even Numbers Using a Generator Function
def odd_even(l):
    for i in l:
        if i%2 == 0:
            yield f"{i} is even "
        else: 
            yield f"{i} is odd "

num = [int(i) for i in input("Enter the numver ").split(",")]
even_odd_object = odd_even(num)
for i in even_odd_object:
    print(i)
