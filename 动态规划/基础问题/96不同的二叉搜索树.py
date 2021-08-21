"""

给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

示例 1：
输入：n = 3
输出：5

示例 2：
输入：n = 1
输出：1

"""


def numTrees(n):

    def Combinatorial(x, i):
        temp = min(i, x - i)
        res = 1
        for j in range(temp):
            res = res * (x - j) / (temp - j)
        return res

    ans = Combinatorial(2 * n, n) - Combinatorial(2 * n, n - 1)
    if ans % 1 > 0.5:
        return int(ans) + 1
    else:
        return int(ans)


print(numTrees(3))
print(numTrees(1))
print(numTrees(4))
print(numTrees(7))
