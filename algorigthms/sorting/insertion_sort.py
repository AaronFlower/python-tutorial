def insertion_sort(na):
	''' 关于 insertion sort 要信手拈来 '''
	length = len(na)
	for i in range(1, length):
		j = i
		while j >= 1 and na[j] < na[j-1]:
			tmp = na[j]
			na[j] = na[j - 1]
			na[j - 1] = tmp
			j -= 1

na = [9, 7, 4, 1, 89, 12, 12, 2]
print('Before sorting:', na)
insertion_sort(na)
print('After  sorting:', na)
