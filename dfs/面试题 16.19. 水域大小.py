"""

你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。
若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。
编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

示例：
输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]

"""


def pondSizes(land):
    ans = []
    n = len(land)
    m = len(land[0])
    fangxiang = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    def dfs(x, y):
        land[x][y] = 1
        c = 1
        for i in range(len(fangxiang)):
            if 0 <= x + fangxiang[i][0] < n and 0 <= y + fangxiang[i][1] < m and land[x + fangxiang[i][0]][y + fangxiang[i][1]] == 0:
                c += dfs(x + fangxiang[i][0], y + fangxiang[i][1])
        return c

    for i in range(n):
        for j in range(m):
            if land[i][j] == 0:
                count = dfs(i, j)
                ans.append(count)
    ans.sort()
    return ans


print(pondSizes([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]))
