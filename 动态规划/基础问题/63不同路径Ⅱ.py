"""

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

示例 2：
输入：obstacleGrid = [[0,1],[0,0]]
输出：1

"""


# 进阶版，难题
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    # 设置一个标志记录障碍
    tag = False

    # 初始化第一行和第一列为1(无障碍)
    for i in range(n):
        # 若第一行某个位置有障碍物，那么该位置及右方都无法到达了
        if obstacleGrid[0][i]:
            # 有障碍，更改标志
            tag = True
        if not tag:
            obstacleGrid[0][i] = 1
        else:
            obstacleGrid[0][i] = 0

    # 判断[0, 0]处是否有障碍物
    tag = not obstacleGrid[0][0]
    for i in range(1, m):
        # 若第一列某个位置有障碍物，那么该位置及下方都无法到达了
        if obstacleGrid[i][0]:
            tag = True
        if tag:
            obstacleGrid[i][0] = 0
        else:
            obstacleGrid[i][0] = 1

    # 逐行计算路径数
    # 当前位置路径数(无障碍) = 上一格路径数 + 左一格路径数
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j]:
                obstacleGrid[i][j] = 0
            else:
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

    return obstacleGrid[-1][-1]


print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(uniquePathsWithObstacles([[0, 1], [0, 0]]))
