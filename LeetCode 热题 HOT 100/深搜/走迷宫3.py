# 题目描述
# 一个迷宫由R行C列格子组成，有的格子里有障碍物，不能走；有的格子是空地，可以走。
# 给定一个迷宫，求从左上角走到右下角最少需要走多少步(数据保证一定能走到)。只能在水平方向或垂直方向走，不能斜着走。

# 输入
# 第一行是两个整数，Ｒ和Ｃ，代表迷宫的长和宽。（ 1≤ R，C ≤ 40)
# 接下来是Ｒ行，每行Ｃ个字符，代表整个迷宫。
# 空地格子用‘.’表示，有障碍物的格子用‘  # ’表示。
# 迷宫左上角和右下角都是‘.’。

# 输出
# 输出从左上角走到右下角至少要经过多少步（即至少要经过多少个空地格子）。计算步数要包括起点和终点。

# 样例输入
# 5 5
# ..###
# #....
# #.#.#
# #.#.#
# #.#..

# 样例输出
# 9


from collections import deque

n, m = map(int, input().split())
migong = []
for i in range(n):
    temp = input()
    migong.append(list(temp))

q = deque([(0, 0)])
g = [[""] * m for _ in range(n)]

while q:
    x, y = q.popleft()
    if x == n - 1 and y == m - 1:
        print(len(g[-1][-1]) + 1)
        break
    for i, j, k in [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]:
        a = x + i
        b = y + j
        if 0 <= a < n and 0 <= b < m and migong[a][b] == '.':
            migong[a][b] = "#"
            q.append((a, b))
            g[a][b] = g[x][y] + k
