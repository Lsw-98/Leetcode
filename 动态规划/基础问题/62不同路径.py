"""

一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6

"""


# 把dp[i][j]上面的各自中的路径数与左面格子的路径数加起来
def uniquePaths(m, n):
    if n == 1 or m == 1:
        return 1
    else:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0
        dp[1][0] = 1
        dp[0][1] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


print(uniquePaths(1, 2))
print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(7, 3))
print(uniquePaths(3, 3))
