# def 函数名(参数):
def hello(a, b):
    print(b, "hello world", a)


# wo hello world wc
hello(b = "wo", a = "wc")

# 建议参数类型是int，如果强行传两个字符串，也能执行，传一个字符串一个数字就会报错
def add(a: int, b: int):
    """
    将两个数字相加
    :param a:
    :param b:
    :return:
    """
    return a + b

# 3
print(add(1, 2))
# 对add函数进行说明
help(add)

# 全局变量a
a = 1
def test():
    # 局部变量
    b = 2
    # 函数内部想要修改全局变量?
    # 使用global对变量进行声明，可通过函数修改全局变量的值
    global a
    a = 5

    print("locals = {}, globals = {}".format(locals(), globals()))


# 调用test()函数，test()函数中对a进行了修改
# 内置函数 globals()、locals()可以查看全局变量和局部变量，打印的locals、globals为：
# locals = {'b': 2}, globals = {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002E13B7D1CC0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/Users/LSD/Desktop/python/py/function/01-函数基本使用.py', '__cached__': None, 'hello': <function hello at 0x000002E13B80C268>, 'add': <function add at 0x000002E13BB43400>, 'a': 5, 'test': <function test at 0x000002E13CB267B8>}
test()
# 5
print(a)

# python里，只有函数能够分隔作用域





def test3(b ,a):
    x = a // b
    y = a % b
    # return [x, y] 可以返回一个列表
    # return {"x": x, "y": y} 可以返回一个字典
    return x, y # 本质是返回一个元组


shang, yushu = test2(16, 3)
# 商是5, 余数是1
print("商是{}, 余数是{}".format(shang, yushu))


def say_hello(name, age = 20):
    print("大家好，我是{}，今年{}岁".format(name, age))


# age指定了默认值，调用时就可以不传，不传就取默认值，如果不设默认值，并且不传，就会报错
say_hello("张三")
# 关键字参数一定放在位置参数后边
say_hello("lisi", age=19)

# 可变参数：*args
def add(a, b, *args):
    print("a = {},b = {}".format(a, b))
    print("args = {}".format(args))


add(1, 2)
add(1, 2, 3)


# python里不允许函数重名，如果重名了，后一个函数会覆盖前一个函数




# 匿名函数
fun = lambda a, b: a + b

students = [
    {"name": "zhangsan", "age":18, "score":20},
    {"name": "zhangsan", "age":18, "score":20},
    {"name": "zhangsan", "age":18, "score":20},
    {"name": "zhangsan", "age":18, "score":20}
]
def foo(ele):
    # 通过返回值，告诉sort方法按照那个参数进行排序
    return ele["age"]


# 排序字典，直接调用sort会报错，因为字典直接不能使用比较运算
# 在sort内部实现中，调用了foo方法，并且传入了一个参数，参数就是列表里的元素
students.sort(key=foo)
# 使用匿名函数，完成类似功能
students.sort(key=lambda ele: ele['score'])


