# 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​，计算并返回两整数之和。

# 示例 1：
# 输入：a = 1, b = 2
# 输出：3

# 示例 2：
# 输入：a = 2, b = 3
# 输出：5


from math import log2
from re import T
from typing import Match


def getSum(a, b):
  # import math
  # # 数学方法
  # a = math.pow(2, a)
  # b = math.pow(2, b)
  # return int(math.log2(a * b))

  # 位运算
  """
    a + b 可以转换为二进制加减，通过位运算 ^ 和 & 进行
    1、通过 & 可知道两数相加后需要进位的部分（a & b -> 0010）然后我们进位 (a & b) << 1 -> 0100，记结果为 i
    2、通过 ^ 可知两数相加后无需进位的部分(a ^ b -> 0101)，记结果为 j
  """
  if a == 0:
    return b
  if b == 0:
    return a
  
  while b != 0:
    temp = a & b
    a = a ^ b
    b = temp << 1
  return a


print(getSum(1, 2))
print(getSum(2, 3))
print(getSum(-1, 1))
