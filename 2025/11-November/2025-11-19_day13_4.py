#armstrong number

num = int(input("Enter number : "))

n = len(str(num))
sum = 0 
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if num == sum:
    print("armstrong")
else:
    print("not armstrong")

