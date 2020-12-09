age = input("请输入年龄：")
# int()转换成int类型
new_age = int(age)
print(new_age + 1)

x = "1a2"
# 418 转换使用16进制
print(int(x, 16))

y = "12.34"
# 12.34
print(float(y))

c = 100
# 100.0
print(float(c))

p = 34
q = str(p)
# <class 'int'>
print(type(p))
# <class 'str'>
print(type(q))

# 数字里，0为False，非0为true
# 字符串里，""为False,None也为False
# []    空列表也为False
# ()    空元组也是False
# {}    空字典也是False
# set() 空集合也是False
# True
print(bool(100))
# False
print(bool(0))
# True
print(bool(-1))
# False
print(bool(''))
# False
print(bool(None))
# False  空列表
print(bool([]))
# False  空字典
print(bool({}))
# False  空元组
print(bool(()))
# False  空集合
s = set()
print(bool(s))

# 2
print(True + 1)
# 1
print(False + 1)