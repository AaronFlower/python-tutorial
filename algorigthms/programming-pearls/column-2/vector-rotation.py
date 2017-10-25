def vector_rotation(str, pos):
	''' 对 str vector 从 pos 的位置开始进行 rotation 
			方法是类似于 transpose 的变换的思路，即 (A.T B.T).T = (BA) 
	''' 
	r_str = str[0:pos][::-1]
	r_str += str[pos:][::-1]
	return r_str[::-1]


def swap(str_list, begin, end):
	''' to be continued
	'''
	half = int((end - begin) / 2) + begin
	for i in range(begin, half):
		tmp = str_list[i]
		str_list[i] = str_list[end - begin - 1 -i]
		str_list[end - begin - 1 - i] = tmp

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

	l_half = int(pos / 2)
	for i in range(l_half):
		tmp = str_list[i]
		str_list[i] = str_list[pos - i - 1]
		str_list[pos - i - 1] = tmp
	
	r_half = int((pos + len(str_list)) / 2)
	for i in range(pos, r_half):
		tmp = str_list[i]
		str_list[i] = str_list[length - 1 - i + pos]
		str_list[length - 1 - i + pos] = tmp

	half = int(length / 2)
	for i in range(half):
		tmp = str_list[i]
		str_list[i] = str_list[length - 1 - i]
		str_list[length - 1 - i] = tmp

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

l_str = list(str)
# swap(l_str, 0, 3)
print(l_str)
swap(l_str, 3, 8)
print(l_str)
