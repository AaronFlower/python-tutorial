# Python Object-Oriented Programming

class Employee:
	pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

# Person class with variables and methods.

class Person(object):
	"""docstring for Person"""

	# class variables and instance variables.
	raise_amount = 1.04
	num_of_persons = 0


	def __init__(self, first, last, pay):
		'''Construtor'''
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' +last + '@company.com'

		Person.num_of_persons += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


# test statements.

p_1 = Person('Eason', 'Zhan', 500000)
p_2 = Person('Musuet', 'Ozil', 600000)

print(p_1.fullname())	 # don't need to pass self.
print(p_2.fullname())	 # don't need to pass self.
print(Person.fullname(p_1)) # pass a self.
print(p_1.pay)
p_1.apply_raise()
print(p_1.pay)

print(Person.raise_amount)
print(p_1.raise_amount)
print(p_2.raise_amount)

print(p_1.__dict__)
print('Class Person __dict__')
print(Person.__dict__)

Person.raise_amount = 1.08
p_1.raise_amount = 1.09

print(Person.raise_amount)
print(p_1.raise_amount)
print(p_2.raise_amount)

print(Person.num_of_persons)


