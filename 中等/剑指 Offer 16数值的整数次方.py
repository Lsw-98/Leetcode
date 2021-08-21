"""

实现pow(x,n)，即计算 x 的 n 次幂函数（即，x ** n）。不得使用库函数，同时不需要考虑大数问题。


示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000

示例 2：
输入：x = 2.10000, n = 3
输出：9.26100

示例 3：
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25

"""


def myPow(x, n):
    if n < 0:
        temp = abs(n)
        ans = 1
        while temp:
            if temp & 1:
                ans *= x
            x *= x
            temp >>= 1
        # return "{:.5f}".format(1 / ans)
        return 1 / ans
    else:
        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        # return "{:.5f}".format(ans)
        return ans


print(myPow(2.00000, 10))
print(myPow(2.10000, 3))
print(myPow(2.00000, -2))
