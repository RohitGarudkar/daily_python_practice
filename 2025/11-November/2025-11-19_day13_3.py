#dictonery functoins

student = {'name':'Rohit','age':21,'subject':'python',}
print(student)

print(student.get('age'))

student['name'] = 'shivam'
print(student)

student['vergin'] = 'True'
print(student)

student.pop('vergin')
print(student)

student.popitem()
print(student)

print(student.items())


#unique list

from array import array

s = 'python'
arr = array('u',s)

arr.append('z')
print(arr)

arr.remove('z')
print(arr)

arr[0] = 'j'
print(arr)

new_str = "".join(arr)
print(type(new_str))
