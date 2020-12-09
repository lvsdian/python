# ord:字符获取编码，chr:编码获取字符
# 97
print(ord("a"))
# a
print(chr(97))

# b'\xc4\xe3'  GBK:一个汉字占两个字节
print("你".encode("gbk"))
# b'\xe4\xbd\xa0'   GBK:一个汉字占三个字节
print("你".encode("utf-8"))


y = "你好".encode("utf-8")
# b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(y)
# 浣犲ソ
print(y.decode("gbk"))