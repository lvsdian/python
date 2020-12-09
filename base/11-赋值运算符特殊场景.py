m, n = 1, 2 #拆包，如果拆包时变量个数与值的个数不一致会报错
# 1 2
print(m, n)

x = "hello", "world", "woc"
# ('hello', 'world', 'woc')
print(x)

# *表示可变，o对应一个，q对应一个，剩下的全是p
o,*p,q = 1, 2, 3, 4, 5, 6
# 1 [2, 3, 4, 5] 6
print(o, p, q)