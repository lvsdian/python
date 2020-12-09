# python2里 != 和 <> 都表示不等于
# python3里只能用 !=

# False
print("a" > "b")

# False  a 和 b 比，为False，就直接返回了
print("abc" > "b")

# 字符串和数字比，!= 返回True，==返回False，其他运算符报错
#print("a" > 90)
print("a" == 90)
print("b" != 90)
