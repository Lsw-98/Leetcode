# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 示例 1：
# 输入：n = 2
# 输出：2

# 示例 2：
# 输入：n = 7
# 输出：21

# 示例 3：
# 输入：n = 0
# 输出：1


def numWays(n):
  dp = [1 for _ in range(n + 1)]
  if n == 0:
    return 1
  if n == 1:
    return 1
  for i in range(2, len(dp)):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
  return dp[-1]


print(numWays(2))
print(numWays(7))
print(numWays(0))
