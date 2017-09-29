# use def to create function.

def pass_func():
	pass # don't execute any code.

print(pass_func)
pass_func()

def hello_func():
	print('Hello function!')

hello_func()

# DRY, Don't repeat yourself.

def foo_func(greeting, name = 'You'):
	return '{} {}.'.format(greeting, name)

print(foo_func('Hi'))
print(foo_func('Hi', ' Eason'))
print(foo_func('Hi', name = ' Eason'))

# args and key-word args
def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

print('*args and **kwargs:')
student_info('Math', 'Art', name = 'John', age = 22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

print('without * and **')
student_info(courses, info)
# * to unpack tuples
# ** to unpack dict
print('with * and ** to unpack those values.')
student_info(*courses, **info)