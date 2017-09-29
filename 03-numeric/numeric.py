num = 1
pi = 3.14
print(num, type(num))
print(pi, type(pi))

# Arithmatic operations
# Floor Division: //
# Exponent **
# Module: %
print(3 / 2) # 
print(3 // 2) # drop decimal 整除
print(3 % 2) # mod
print('power:', 3 ** 2)

# Build-in funciton: abs, round
print('abs:', abs(-5))
print('round:', round(-5.12, 1), round(-5.12))

# comparison
print(num == pi, num != pi, num <= pi)

# parse, casting
num_1 = '100'
num_2 = '200'
print(num_1 + num_2, int(num_1) + int(num_2))
