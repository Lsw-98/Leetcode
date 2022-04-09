# 题目描述
# 给定一个 Ntimes MN×M 的网格迷宫 GG。GG 的每个格子要么是道路，要么是障碍物（道路用 11 表示，障碍物用 00 表示）。

# 已知迷宫的入口位置为(x1​, y1)，出口位置为(x2​, y2)。问从入口走到出口，最少要走多少个格子。

# 输入描述
# 输入第 1 行包含两个正整数 N, M，分别表示迷宫的大小。

# 接下来输入一个 N×M 的矩阵。若 Gij=1 表示其为道路，否则表示其为障碍物。

# 最后一行输入四个整数 x1, y1, x2, y2表示入口的位置和出口的位置。

# 输出描述
# 输出仅一行，包含一个整数表示答案。

# 若无法从入口到出口，则输出 −1。

# 输入输出样例
# 示例 1
# 输入
# 5 5
# 1 0 1 1 0
# 1 1 0 1 1
# 0 1 0 1 1
# 1 1 1 1 1
# 1 0 0 0 1
# 1 1 5 5

# 输出
# 8


from collections import deque
n, m = map(int, input().split())
migong = []
for i in range(n):
    temp = list(map(int, input().split()))
    migong.append(temp[:m])
x1, y1, x2, y2 = map(int, input().split())
g = [[""] * m for _ in range(n)]
q = deque([(x1 - 1, y1 - 1)])
while q:
    x, y = q.popleft()
    if x == x2 - 1 and y == y2 - 1:
        print(len(g[x][y]))
        break
    for i, j, k in [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]:
        a = x + i
        b = y + j
        if 0 <= a < n and 0 <= b < m and migong[a][b] == 1:
            q.append((a, b))
            migong[a][b] = 0
            g[a][b] = g[x][y] + k
if x != x2 - 1 and y != y2 - 1:
    print(-1)
