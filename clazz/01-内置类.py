from functools import reduce

# filter 过滤，在python2的时候是内置函数，python3修改成了一个内置类
ages = [11, 22, 33, 44, 55]
# filter可以给定两个参数，一个是函数，一个是可迭代对象
# filter结果是一个filter类型的对象，filter对象也是一个可迭代对象
x = filter(lambda ele: ele > 18, ages)
# <filter object at 0x0000016765218160>
print(x)
# [22, 33, 44, 55]
print(list(x))
# 类似的还有map
# 内置函数和内置类都在builtins.py里

ages = [1, 2, 3, 4]
# 10
print(reduce(lambda ele1, ele2: ele1 + ele2, ages))