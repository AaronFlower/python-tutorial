import random
def quick_sort(na, begin, end):
	if end - begin > 1:
		i = partition(na, begin, end)
		quick_sort(na, begin, i)
		quick_sort(na, i + 1, end)

def swap(na, i, j):
	tmp = na[i]
	na[i] = na[j]
	na[j] = tmp

def partition(na, begin, end):
	''' 
		选择一个 pivot ，partition 结束后，na[小于 pivot, pivot, 大于 pivot]，
		如果是其它功能的 partion 可能不关心 pivot 的位置，只关心分成两部分即可。
	'''
	pivotIndex = random.randrange(begin, end)
	pivot = na[pivotIndex]
	lastIndex = end - 1
	swap(na, pivotIndex, lastIndex) # 保证 pivot 在最后一个元素上。

	i = begin - 1
	j = begin
	while j < lastIndex:
		if na[j] <= pivot:
			i += 1
			swap(na, j, i)
		j += 1
	swap(na, i + 1, lastIndex)
	return i + 1


na = [3, 4, 7, 6, 2, 1]
# i, pivot = partition(na, 0, len(na))
quick_sort(na, 0, len(na))
print(na)
# print(i, pivot)