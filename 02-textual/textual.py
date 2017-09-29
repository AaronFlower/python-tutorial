msg = 'Hello world'
msg2 = """This is 
a paragraph"""
print(msg2, msg2[1], len(msg2))

# slicing a string
print(msg, msg[0], len(msg), msg[:5], msg[0:5], msg[6:])
# reverse a string by [begin:end:step]
# step 为正数是步长，为 -1 时是 reverse
print('Origin a string:', msg[::])
print('Reverse a string:', msg[::-1])
print('Step 2 a string:', msg[::2])

# member methods
print(msg.upper(), msg.lower(), msg.count('d'))


# replace
print(msg.replace('world', 'universe'))

# 
greeting = 'Hello'
name = 'eason'

msg = '{}, {}. Welcome'.format(greeting, name)
new_msg = f'{greeting}, {name.upper()}, Welcome!'
print(msg)
print(new_msg)

# dir function. all attributes. help funciton.
print(dir(msg))
# help funtion
# print(help(str))
print (help(str.lower))
