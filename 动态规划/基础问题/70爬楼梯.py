"""

假设你正在爬楼梯。需要 n阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

"""


def climbStairs(n):

    # f1, f2 = 1, 1
    # for i in range(n):
    #     f2 = f1 + f2
    #     f1 = f2 - f1
    # return f1
    
    # 动态规划
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(5))
print(climbStairs(10))
print(climbStairs(100))
