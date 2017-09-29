nums = [1, 2, 3, 4, 5]

for num in nums:
	print(num)

print('break state:')
for num in nums:
	if num == 3:
		print('Found!')
		break
	print(num)

print('continue state:')
for num in nums:
	if num == 3:
		print('Found!')
		continue
	print(num)


# nested loops
print('nested loops:')
for num in range(1, 2):
	for letter in 'abc':
		print(num, letter)

# while
print('while state:')
x = 0
while x < 3:
	print(x)
	x += 1