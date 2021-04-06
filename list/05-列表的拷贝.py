import copy

# 深拷贝，只能用copy模块实现
words = ["hello", "world", [1, 2, 3]]

# words1是words的浅拷贝
workds1 = words.copy()

# workds2是深拷贝
workds2 = copy.deepcopy(words)