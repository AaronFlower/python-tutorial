# True
# Equal ==
# Not Equal !=
# Object Identity: is. the same id.

# not and or.

# python no switch case.
language = 'python'
if language == 'python':
	print('Coditional waw True')
elif language == 'Java':
	print('language is Java')
else:
	print('No match!')

# is

a = [1, 2, 3]
b = [1, 2, 3]
c = b
print('a == b:', a == b)
print(id(a))
print(id(b))
print(id(c))
print('a is b:', a is b)
print('c is b:', c is b)

# False values:
# False
# None
# Zero of any numeric type
# Any empty sequence. E.g. '', (), []
# Aay empty mapping. E.g. {}

if False or None or 0 or 0.0 or '' or () or [] or {} :
	print('Evaluated to True.')
else:
	print('Evaluated to False.')
