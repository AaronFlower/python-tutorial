student = {
	'name': 'Jhon',
	'age': 25,
	'courses': ['Math', 'ComSci']
}
print(student)
print(student['name'])
# print(student['phone'])
# 用 get 方法来避免 KeyError
print(student.get('name'), student.get('phone'))
student['phone'] = '021-231231'
print(student.get('name'), student.get('phone'))

# update key in batch
student.update({'name': 'Eason', 'phone': '011-9999'})

# del
del student['age']
print(student, student.get('age'))

# pop
popped = student.pop('phone')
print(student, popped)

# len, keys, 
print(len(student), student.keys())
print(len(student), student.values())
print(len(student), student.items())

for key, value in student.items():
	print('key-value:', key, value)