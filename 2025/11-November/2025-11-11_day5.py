#LIST AND OPERATIONS 

marks = [2,1,3]
marks.append(4)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(0,0)
print(marks)
marks.remove(0)
print(marks)
marks.pop(0)
print(marks)
marks.insert(0,1)
print(marks)

list = ['a','b','c','d']
print(list)
list.insert(0,'R')
print(list)
list.remove('R')
print(list)


a = [2,1,3]
a[0] = 99
print(a)

#LIST AND TUPLES 

marks = [10,20,30,40,50,60,70,80,90]
print(marks)
print(marks[-3:-1])
print(marks[2])

list = [1,2,3,4]
tup = (1,2,3,4)
print(type(list))
print(type(tup))

list [0] = 99
print(list)
# tup [0] = 99     #does not support item assignment
print(tup)

