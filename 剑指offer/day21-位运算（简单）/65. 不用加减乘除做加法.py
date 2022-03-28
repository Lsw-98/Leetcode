# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

# 示例:
# 输入: a = 1, b = 1
# 输出: 2


def add(a, b):
  while b:
    temp = (a & b) << 1
    a ^= b
    b = temp
  return a


print(add(-1, 2))
