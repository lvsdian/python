# pass关键字在Python里没有意义，只是用来占位，保证语句的完整性

age = int(input("请输入年龄："))
# 如下，报错
# if age < 18:
# print("睡觉")

# pass占位
if age < 18:
    pass
print("睡觉")