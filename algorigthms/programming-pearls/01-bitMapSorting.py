'''
有 10^7 个惟一数字存在一个文件中，规定只能使用不超过 1MB 的内存来完成排序怎么实现？
用  bitMap 来完成排序。
Precise Problem Statement.
Input 	A file containing at most n positive integers, each less than n, where n = 10^7.
				It is a fatal error if any integer occurs twice in the input. No other data is associated
				with the integer.

Output 	A sorted list in increasing order of the input integers.

Constraints 	At most(roughly) a megabyte of storage is available in main memory; ample disk storage is 
							available. The run time can be at most serveral minutes; a run time of ten seconds need not 
							be decreased.
'''
from bitarray import bitarray
import random

''' 下面用一个简单数据集来完成测试。'''

MAX_SIZE = 1024

def generate_data (len):
	''' 随机生成输入数据'''
	return random.sample(range(len), len)

def bit_map_sort(data):
	bit_map = bitarray(MAX_SIZE)
	bit_map.setall(0)
	for d in data:
		bit_map[d] = 1
	
	data = []
	i = -1
	for b in bit_map:
		i += 1
		if b: data.append(i)

	return data

bm = bitarray(10)
bm.setall(0)
print(bm[0], bm[1], bm)
data = generate_data(10)
print('Before sorting: ')
print(data)
print('After sorting: ')
data = bit_map_sort(data)
print(data)

data = [23, 68, 90, 223, 12, 33, 22, 110]
print('\nBefore sorting: ')
print(data)
data = bit_map_sort(data)
print('After sorting:')
print(data)

