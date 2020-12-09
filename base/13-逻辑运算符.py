# 与and 或or 非not
# False
print(not(5 > 2))

# 0   取第一个遇到的False
print(3 and 2 and 1 and 0 and "hello")
# 1   如果都为True，取最后一个值
print(3 and 2 and 1)

# hello   取第一个遇到的True
print(() or {} or [] or 0 or "hello")
# []   如果都为False，取最后一个值
print(() or {} or [])