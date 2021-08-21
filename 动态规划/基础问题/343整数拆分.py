"""

给定一个正整数n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 ×3 ×4 = 36。

"""


# 基本思路 dp[i]代表是i被拆分至少两个正整数的和之后，这些正整数的最大乘积
# 当 i≥2 时，假设对正整数 i 拆分出的第一个正整数是 j（1≤j<i），则有以下两种方案：
# 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j×(i−j)；
# 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j×dp[i−j]。

def integerBreak(n):
    # dp = [0 for _ in range(n + 1)]
    # dp[0] = dp[1] = 0
    # for i in range(2, n + 1):
    #     for j in range(i):
    #         dp[i] = max(dp[i], (j * (i - j)), (j * dp[i - j]))
    # return dp[n]

    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 4
    elif n == 5:
        return 6
    elif n == 6:
        return 9
    else:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        dp[5] = 6
        dp[6] = 9
        for i in range(7, n + 1):
            dp[i] = dp[i - 3] * 3
        return dp[n]


print(integerBreak(2))
print(integerBreak(10))
