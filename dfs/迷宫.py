"""

题目背景
给定一个N*M方格的迷宫，迷宫里有T处障碍，障碍处不可通过。给定起点坐标和终点坐标，
每个方格最多经过1次，有多少种从起点坐标到终点坐标的方案。在迷宫中移动有上下左右四种方式，每次只能移动一个方格。
数据保证起点上没有障碍。

输入格式
第一行N、M和T，N为行，M为列，T为障碍总数。第二行起点坐标SX,SY，终点坐标FX,FY。接下来T行，每行为障碍点的坐标。

输出格式
给定起点坐标和终点坐标，问每个方格最多经过1次，从起点坐标到终点坐标的方案总数。

输入输出样例
输入
2 2 1
1 1 2 2
1 2
输出
1

-1 1 1
1  1 1
1  1 -2

"""

"""

伪代码
dfs(x, y):
    if 这个点是终点:
        count += 1
        return
    标记(x, y)已走过，枚举下一步要走的点
    if 这个点能走:
        dfs(下一个点)
    取消(x, y)标记
"""


n, m, t = map(int, input().split())
sx, sy, fx, fy = map(int, input().split())
zhangai = []
for _ in range(t):
    zhangai.append(list(map(int, input().split())))

migong = [[0] * m for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            # 起点是-1
            migong[i][j] = -1
        # elif i == n - 1 and j == m - 1:
        #     # 终点是-2
        #     migong[i][j] = -2
        elif i == zhangai[count][0] - 1 and j == zhangai[count][1] - 1:
            # 障碍是-3
            migong[i][j] = -3
ans = 0


def dfs(x, y):
    global ans
    if x == fx - 1 and y == fy - 1:
        ans += 1
        return

    migong[x][y] = 1
    if x - 1 >= 0:
        if migong[x - 1][y] == 0:
            dfs(x - 1, y)
    if x + 1 < n:
        if migong[x + 1][y] == 0:
            dfs(x + 1, y)
    if y - 1 >= 0:
        if migong[x][y - 1] == 0:
            dfs(x, y - 1)
    if y + 1 < m:
        if migong[x][y + 1] == 0:
            dfs(x, y + 1)
    migong[x][y] = 0
    return


dfs(sx - 1, sy - 1)
print(ans)
