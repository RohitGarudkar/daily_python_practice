#dictionary functions

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
