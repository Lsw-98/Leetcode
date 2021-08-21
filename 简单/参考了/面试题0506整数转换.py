"""

整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。

示例1:
输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
输出：2

示例2:
输入：A = 1，B = 2
输出：2

提示:
A，B范围在[-2147483648, 2147483647]之间

"""


def convertInteger(A, B):
    # &:位与运算符，表示a为真且b为真，该位才同时为真
    # 让任意一个整数 n & 0xFFFF FFFF 就能表示出任意一个数在计算机的表示方式！
    # 求二进制
    A &= 0xFFFFFFFF
    B &= 0xFFFFFFFF
    print(A)
    # 异或操作
    res = A ^ B
    count = 0
    while res:
        res &= res - 1
        count += 1
    return count


print(convertInteger(1, 2))
print(convertInteger(29, 15))
print(convertInteger(826966453, -729934991))
