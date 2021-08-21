"""

三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，
计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例 1:
 输入：n = 3
 输出：4
 说明: 有四种走法

示例 2:
 输入：n = 5
 输出：13

"""


def waysToStep(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        for i in range(3, n):
            dp[i] = dp[i - 1] % 1000000007 + dp[i - 2] % 1000000007 + dp[i - 3] % 1000000007
        return dp[-1] % 1000000007


print(waysToStep(3))
print(waysToStep(5))
