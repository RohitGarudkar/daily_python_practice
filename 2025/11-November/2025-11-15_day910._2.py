#for loop
num = [45,454,68,86,75,46,876] 
for i in num:
    print(i)

print("\n------------\n")

st = "Rohit harish garudkar"
for i in st:
    if (i == 'h'):
        continue
    print(i)
else:
    print("else block loop ended...")

print("\n----------------\n")
i = 3
j = 1
for x in range(1,i+1):
    j*=x 
print(j)
