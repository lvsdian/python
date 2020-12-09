# str list tuple可以通过下标来获取或者操作数据
words = "hello world"
# l
print(words[2])

# 切片就是从字符串里复制一段指定的内容，生成一个新的字符串
# ell  左闭右开
print(words[1:4])
# o world 从4到最后，包含4
print(words[4:])
# hell 从头到4，不包含4
print(words[:4])
# hlow 从0-8，步长为2，默认步长为1,步长不能为0
print(words[0:8:2])
# olle 步长可以为负数，即从右往左走，右边边界包含，左边边界不包含
print(words[4:0:-1])
# 从头到尾
print(words[::])
# 从尾到头
print(words[::-1])
# 从右往左第六个 到 从右往左第二个，步长为1
print(words[-6:-2])