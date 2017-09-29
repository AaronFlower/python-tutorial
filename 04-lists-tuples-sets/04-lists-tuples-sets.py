# lists
courses = ['history', 'math', 'physics', 'CompSci']
courses_2 = ['Printing', 'Education']
# 可以使用 negative number
print(len(courses), courses, courses[1], courses[2:], courses[-1])
# range slicing
print(courses[0:2], courses[:2]) 
# reverse & sorting
print(courses[::-1], courses.reverse(), courses.sort()) 

# methods, adding
courses.append('Art')
print(courses)
courses.insert(0, 'Chemistry')
print(courses)
courses.extend(courses_2)
print(courses)

# methods, removing
courses.remove('math')
print(courses)
popped = courses.pop() # remove the last one
print(courses, popped)

# sorting
nums = [1, 5, 2, 4, 3]
nums_2 = [1, 5, 2, 4, 3]
nums.sort()
nums_2.sort(reverse = True)
print(nums)
print(nums_2)
print(min(nums), max(nums))

# sorted function
sorted_courses = sorted(courses)
print(sorted_courses)

# find index
print('index:', courses.index('Art'))
#print('index:', courses.index('Art-'))
print('Math' in courses, 'Art' in courses)

for item in courses:
	print('courses list:', item)

# enumerate function
for index, course in enumerate(courses):
	print(index, course)

# enumerate function
for index, course in enumerate(courses, start=2):
	print(index, course)

# join
courses_str = ','.join(courses)
new_list = courses_str.split(',')
print(courses_str, new_list)

## Tuples
## 我们无法改变 tuples, tuples 是 immutable, 而 list 是 mutable 的。
courses_1 = ['history', 'math', 'physics', 'CompSci']
courses_2 = courses_1
courses_1.append('Art')
print('courses_1:', courses_1)
print('courses_2:', courses_1)
## tuple 是 immutable, 基它操作和 list 一样。
tuple1_1 = ('history', 'math', 'physics', 'CompSci')
tuple1_2 = tuple1_1
print(tuple1_1[:2])
# tuple1_1[0] = 'Art'
for item in tuple1_1:
	print('tuple :', item)


## sets, sets don't care order
cs_courses = {'history', 'math', 'physics', 'CompSci', 'math'}
art_courses = {'history', 'math', 'Art'}
print(cs_courses) # 每次输出的结果可能不一样。
print('math' in cs_courses)
print('intersection:', cs_courses.intersection(art_courses))
print('difference:', cs_courses.difference(art_courses))
print('union:', cs_courses.union(art_courses))

## create empty lists, tuples, sets
## empty lists
empty_list = []
empty_list = list()
## empty tuples
empty_tuple = ()
empty_tuple = tuple()
## Empty sets
empty_sets = {} # 这不是创建一个 set， 而是创建的是一个 dict
empty_sets = set()



