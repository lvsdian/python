# 使用[]来表示一个列表，列表里的每一个数据我们称之为元素
# 元素之间用逗号进行分割
names1 = ["张三", "李四", "王五", "赵六"]

# 可以使用list(可迭代对象),将可迭代对象转换为一个列表
names2 = list(("兰陵王", "张飞", "马超"))

# 和字符串一样，都可以使用下标来获取元素和对元素进行切片
# ['李四']
print(names1[1:2])

# 同时，可以使用下标来修改列表里的元素-----字符串不可修改，list可以修改
names1[3] = "花木兰"
# ['张三', '李四', '王五', '花木兰']
print(names1)

heros = ["亚瑟", "韩信", "李白"]

heros.append("黄忠")
# ['亚瑟', '韩信', '李白', '黄忠']
print(heros)

heros.insert(2, "盘古")
# ['亚瑟', '韩信', '盘古', '李白', '黄忠']
print(heros)

heros.extend(("马克", "米莱迪"))
# ['亚瑟', '韩信', '盘古', '李白', '黄忠', '马克', '米莱迪']
print(heros)

x = heros.pop()
# 米莱迪
print(x)
# ['亚瑟', '韩信', '盘古', '李白', '黄忠', '马克']
print(heros)

x = heros.pop(0)
# 亚瑟
print(x)
# ['韩信', '盘古', '李白', '黄忠', '马克']
print(heros)

x = heros.remove("马克")
# None
print(x)
# ['韩信', '盘古', '李白', '黄忠']
print(heros)

# 2
print(heros.index("李白"))

# 1
print(heros.count("李白"))

# True
print("李白" in heros)

heros[1] = "铠"
# ['韩信', '铠', '李白', '黄忠']   通过下标直接修改
print(heros)

# 遍历  for...in本质是不断地调用next方法
for hero in heros:
    print(hero)


# 排序，反转
heros.sort(reverse=True)
# ['黄忠', '韩信', '铠', '李白']
print(heros)

# 内置函数 sorted()
# sorted()不会改变原有list,会生成一个新的list
print(sorted(heros))
# ['黄忠', '韩信', '铠', '李白']
print(heros)

heros.reverse()
print(heros)
print(heros[::-1])

