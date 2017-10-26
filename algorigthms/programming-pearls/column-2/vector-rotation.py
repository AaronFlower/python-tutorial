def vector_rotation(str, pos):
	''' 对 str vector 从 pos 的位置开始进行 rotation 
			方法是类似于 transpose 的变换的思路，即 (A.T B.T).T = (BA) 
	''' 
	r_str = str[0:pos][::-1]
	r_str += str[pos:][::-1]
	return r_str[::-1]


def str_reverse(str_list, begin, end):
	mid = int((end - begin) / 2) + begin
	loops = mid - begin
	last = end - 1
	for i in range(loops):
		tmp = str_list[begin + i]
		str_list[begin + i] = str_list[last - i]
		str_list[last - i] = tmp


def vector_rotation_2(str, pos):
	''' 自己实现交换? 
			python 里面好像不是那么方便呀！Python 里的字符串是 immutable.
			Python strings cannot be changed — they are immutable. 
			Therefore, assigning to an indexed position in the string results in an error.
		 	那是不是可以直接通过，list 来做那？
		 	注意交换时的 base
	'''
	str_list = list(str)
	length = len(str)
	str_reverse(str_list, 0, pos)
	str_reverse(str_list, pos, length)
	str_reverse(str_list, 0, length)
	return ''.join(str_list)

str = 'abcdefgh'
print(vector_rotation(str, 1))
print(vector_rotation(str, 2))
print(vector_rotation(str, 3))
print(vector_rotation(str, 6))
print('Version 2:')
print(vector_rotation_2(str, 1))
print(vector_rotation_2(str, 2))
print(vector_rotation_2(str, 3))
print(vector_rotation_2(str, 6))
