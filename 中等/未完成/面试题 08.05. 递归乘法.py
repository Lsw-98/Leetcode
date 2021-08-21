"""

递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

示例1:
输入：A = 1, B = 10
输出：10

示例2:
输入：A = 3, B = 4
输出：12

提示:
保证乘法范围不会溢出

"""


def multiply(A, B):
    # 思路1:
    # a * b 相当于b个a相加
    # 缺点就是B大了容易超时
    # res = 0
    # for i in range(B):
    #     res += A
    # return res

    # 思路2:
    pass


print(multiply(1, 10))
print(multiply(3, 4))
