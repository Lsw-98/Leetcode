"""

给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1：
输入：
[[0,0,0],
 [0,1,0],
 [0,0,0]]

输出：
[[0,0,0],
[0,1,0],
[0,0,0]]

示例 2：
输入：
[[0,0,0],
 [0,1,0],
 [1,1,1]]

输出：
[[0,0,0],
 [0,1,0],
 [1,2,1]]

"""


def updateMatrix(matrix):
    dp = [[float("inf")] * len(matrix[0]) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                dp[i][j] = 0

    # 做四次动态规划
    # 我们就可以使用动态规划解决这个问题了。我们用 f(i, j) 表示位置 (i, j) 到最近的 0 的距离。
    # 如果我们只能「水平向左移动」和「竖直向上移动」，那么我们可以向上移动一步，再移动 f(i - 1, j) 步到达某一个 0，
    # 也可以向左移动一步，再移动 f(i, j - 1) 步到达某一个 0。因此我们可以写出如下的状态转移方程
    # f(i, j) = min(f(i - 1, j), f(i, j - 1)) + 1   // 位置(i, j)的元素为 1
    #         = 0                                   // 位置(i, j)的元素为 0

    # 只有 水平向左移动 和 竖直向上移动；
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            if j - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    # 只有 水平向左移动 和 竖直向上移动；
    # for i in range(len(matrix) - 1, -1, -1):
    #     for j in range(len(matrix[0])):
    #         if i + 1 < len(matrix):
    #             dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
    #         if j - 1 >= 0:
    #             dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    # 只有 水平向右移动 和 竖直向下移动；
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(len(matrix[0]) - 1, -1, -1):
            if i + 1 < len(matrix):
                dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
            if j + 1 < len(matrix[0]):
                dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)

    # 只有 水平向右移动 和 竖直向上移动。
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0]) - 1, -1, -1):
    #         if i - 1 >= 0:
    #             dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
    #         if j + 1 < len(matrix[0]):
    #             dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)

    return dp


print(updateMatrix([[0], [1]]))
print(updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
