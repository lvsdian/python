# hello world woc
print("hello", "world", "woc")

# sep参数表示输出时，每个值之间使用哪种字符作为分隔，默认使用空格
# hello+world+woc
print("hello", "world", "woc", sep='+')

# end：当执行完一个print语句后，接下来要输出的字符，默认\n表示换行
# hello world...woc
print("hello", "world", end="...")
print("woc")