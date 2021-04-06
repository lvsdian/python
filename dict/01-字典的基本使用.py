# 列表可以存储任意类型数据，但一般情况下，只存单一数据类型

# 列表只存储值，但无法对值进行描述
# 字典不仅可以保存值，还可以对值进行描述
# 字典里的数据都是以键值对的形式保留的
# key、value之间用:连接
# 多个键值对之间用,分割
person = {
    "name":"zhangsan",
    "age": 18,
    ("x", "y"):"woc",
    "hobbies":["唱", "跳", "rap"]
}

# 字典里的key不能重复，重复了后一个会覆盖前一个
# 字典的value可以使用任意数据类型，但key只能使用不可变数据类型，一般使用字符串

#查 字典的数据在保存时，是无序的，不能通过下标来获取，只能通过key来获取
# 如果key不存在就直接报错了
print(person['name'])

# 使用get方法，如果不存在key，就返回默认值，而不保存
print(person.get('gender', "female"))

# 使用等号，修改key对应的value
person["name"] = "lisi"
# 如果key不存在，会往字典里添加新的键值对

# 删除一个键值对，返回删除的value
person.pop("name")

# 删除一个键值对，返回删除的键值对
person.popitem()

# 清空
# person.clear()

person1 = {
    "name":"zhangsan",
    "age":18
}
person2 = {
    "addr":"襄陽",
    "height":20
}
# 合并两个字典
person1.update(person2)
# 列表、元组可通过加号进行合并，字典用加号就报错
# person1 + person2

# 遍历
# for...in 循环取的是key
for x in person:
    print(x, "=", person[x])

for k in person.keys():
    print(k, "=", person[k])

for v in person.values():
    print(v)

# 列表里面放元组
# dict_items([('age', 18), (('x', 'y'), 'woc')])
print(person.items())

for k, v in person.items():
    print(k, "=", v)