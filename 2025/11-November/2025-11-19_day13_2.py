
#2000 to 3000 all digits are even

for i in range(2000,3001):
    s = str(i)
    all_even = True

    for ch in s:
        if int(ch) % 2 != 0:
            all_even = False
            break
    
    if all_even:
        print(i)
