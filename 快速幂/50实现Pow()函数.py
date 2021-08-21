"""

实现pow(x, n)，即计算 x 的 n 次幂函数（即，x ** n）。

示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000

示例 2：
输入：x = 2.10000, n = 3
输出：9.26100

示例 3：
输入：x = 2.00000, n = -2
输出：0.25000
解释：2 ** -2 = 1/2 ** 2 = 1/4 = 0.25

"""


def myPow(x, n):
    # 自己的解法，很垃圾
    # 时间复杂度：O(n)
    # 而且有一个测试用例会超时(0.00001, 2147483647)
    # if n == 0:
    #     return 1
    # elif n < 0:
    #     x = 1 / x
    #     n *= -1
    # temp = x
    # for i in range(n - 1):
    #     x = x * temp
    # return "%.5lf" % x

    # 参考的算法
    # 快速幂, 时间复杂度：O(logn)
    # 当 x = 0.0时：直接返回 0.0，以避免后续 1 除以 0 操作报错。
    # 初始化 res = 1 。
    # 当 n < 0 时：把问题转化至 n ≥ 0 的范围内，即执行 x = 1 / x ，n = - n。
    # 循环计算：当 n = 0 时跳出。
    # 当 n & 1 = 1时：将当前 x 乘入 res （即 res *= x）。
    # 执行 x = x^2 (即 x *= x)。
    # 执行 n 右移一位(即 n >>= 1)。
    # 返回 res

    from decimal import Decimal
    if x == 0:
        return 0
    else:
        res = 1
        if n < 0:
            x = 1 / x
            n = -n

        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
    return Decimal(res).quantize(Decimal('1.00000'))


print(myPow(2.00000, 10))
print(myPow(0.00001, 2147483647))
