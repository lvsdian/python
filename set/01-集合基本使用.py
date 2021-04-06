import json

# 集合是一个不重复的无序，可以用{}或set来表示
# {}有两种意思：字典、集合
# {}里如果放的是键值对，他就是一个字典，如果放单个值，就是一个集合
names = {"zhangsan", "lisi", "zhangsan"}

# 清空
names.clear()
# {}空集合的表示方式不是{},{}表示的是空字典
print(names)

# 添加一个元素
names.add("阿珂")

# 随机删除一个
names.pop()

# 删除一个指定元素，如果元素不存在，保存
names.remove("阿珂")

# 将多个集合合并生成一个新的集合
names.union({"刘能", "赵四"})

# a.update(b)，将b拼接到a里
names.update({"李白"})
names.update(["张飞"])

print("韩信" in names)

names2 = {"远哥", "玄策"}

# set支持很多的算术运算符
# 不支持加法
# print(names + names2)

# names2有，names没有
print(names2 - names)

# names2,names都有
print(names2 & names)

# names 加上 names2
print(names | names2)

# names独有 加上 names2独有
print(names ^ names2)

# 去重排序
nums = [3, 2, 1, 3, 4, 5, 5]
x = set(nums)
y = list(x)
y.sort(reverse=True)
print(y)

# 使用tuple内位置类转成元组
x = tuple(nums)

# 使用set内置类转成集合
x = set(nums)

z = list({"name":"zhangsan", "age":18, "score":100})

# eval：指定字符串里的代码
a = "1 + 1"
print(eval(a))

# dumps将字典、列表、集合、元组等转成json字符串
# loads将json字符串转换成python里的数据
json.dumps(names)