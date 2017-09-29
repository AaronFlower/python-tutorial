import my_module
import my_module as mm
from my_module import find_index as fi, test
from my_module import * # 引入所有
# 同一个 module 只会被引入一次。

# 引入 module 是检查 sys.path 的
import sys
import random
import os

courses = ['History', 'Math', 'Physics', 'Art']

index = mm.find_index(courses, 'Math')
print(index, fi(courses, 'ComSci'))
print(test)
sys.path.append('/Users/easonzhan/Desktop')
print(sys.path)

print(random.choice(courses), random.choice(courses))
print(os.getcwd())
print(os.__file__)

import antigravity