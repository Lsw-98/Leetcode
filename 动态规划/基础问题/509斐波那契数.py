"""

斐波那契数，通常用F(n) 表示，形成的序列称为 斐波那契数列 。该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1)= 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。

示例 1：
输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1

示例 2：
输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2

示例 3：
输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3

"""


# 快速幂法
def fib(n):
    # 矩阵相乘
    def multi(a, b):
        res = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    res[i][j] = res[i][j] + a[i][k] * b[k][j]
        return res

    base = [[1, 1], [1, 0]]
    ans = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            ans = multi(ans, base)
        base = multi(base, base)
        n >>= 1
    return ans[0][1]


# print(fib(2))
# print(fib(3))
# print(fib(4))
# print(fib(10))
print(fib(100))
