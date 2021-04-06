def outer():
    x = 10 # 在外部函数里定义了一个变量x，是一个局部变量

    def inner():
        # 在内部函数如何修改外部函数的局部变量
        nonlocal x # 用nonlocal,此时，这里的x就是外部函数的局部变量x
        y = x + 1
        print("inner里的y = ", y)
    return inner

# inner里的y =  11
outer()()