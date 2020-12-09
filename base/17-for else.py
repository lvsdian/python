# 当循环里的break没执行时，会执行else
for i in range(10, 20):
    for j in (2, i / 2 + 1):
        if i % j == 0:
            break
    else:
        print(i, "是质数")