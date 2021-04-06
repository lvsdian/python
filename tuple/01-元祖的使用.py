# 元组和列表很像，都是用来保存多个数据
# 使用一对小括号()来表示一对元祖
# 元组和列表的区别在于,列表是可变的，元组是不可变类型(因此可作为字典的key)

nums = (1, 2, 3, 4, 5, 6)
# 0
print(nums.index(1))
# 1
print(nums.count(2))

# 如果元组只有一个元素，要在末尾加逗号
ages = (18,)

# ('h', 'e', 'l', 'l', 'o')
print(tuple("hello"))
# (1, 2, 3, 4, 5, 6)
print(str(nums))

# 合并两个元组
words1 = ("hello", "world")
words2 = ("yes", "ok")
print(words1 + words2)