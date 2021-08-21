"""

设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。

示例:
输入: a = 1, b = 1
输出: 2


提示：
a,b均可能是负数或 0
结果不会溢出 32 位整数

"""


def add(a, b):
    x = 0
    lst = []
    a = bin(a).replace('0b', '')
    b = bin(b).replace('0b', '')
    reversed(a)
    reversed(b)
    # for i in range(min(len(a), len(b))):
    #     lst.append()a[i] ^ b[i]

    return a


print(add(1, 1))
print(add(11, 9))
