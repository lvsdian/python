x = "abcdefg"
print(len(x))

# -1
print(x.find("g", 0, 2))
# 报错
# x.index("h")

# False
print("3.14".isdigit())
# 是否由数字或者字母或数字字母组成
"123abc".isalnum()

x = "1,2,3a,bc"
# ['1', '2', '3a', 'bc']
print(x.split(","))
print(x.rsplit(","))
# ['1', '2', '3a,bc']
print(x.split(",", 2))
# ['1,2', '3a', 'bc']
print(x.rsplit(",", 2))

y = "abcedefd"
# ('abc', 'e', 'defd')
print(y.partition("e"))
# ('abced', 'e', 'fd')
print(y.rpartition("e"))

z = "good morning"
# Abcdef  第一个字母大写
print(z.capitalize())
# Good Morning 每个单词首字母大写
print(z.title())

# ljust:让字符串以指定长度显示，如果长度不够，在右侧默认以空格补齐，rjust类推
# Goods     (Goods后面有5个空格)
print("Goods".ljust(10))
# Goods
print("Goods".ljust(3))
# Goodsxxxxx
print("Goods".ljust(10, "x"))

# **apple***    apple位于中间，左右两侧补齐*
print("apple".center(10, "*"))

# abc
print(" abc".lstrip())
# abc
print("abc ".rstrip())
# abc
print(" abc ".strip())

fruits = ["apple", "pear", "peach"]
# apple-pear-peach
print("-".join(fruits))
# h*e*l*l*o
print("*".join("hello"))