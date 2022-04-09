from collections import deque

n = int(input())
migong = []
for _ in range(n):
    temp = input()
    migong.append(list(temp))
visit = [[0] * n for _ in range(n)]  # 标记列表
flag = True  # 淹没标志
count = 0


def bfs(x, y):
    global flag
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        if migong[x][y+1] == '#' and migong[x][y-1] == '#' and migong[x+1][y] == '#' and migong[x-1][y] == '#':
            flag = False   # 如果格子的四周有岛屿，中间就不会被淹没
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            a = x + i
            b = y + j
            if visit[a][b] == 0 and migong[a][b] == "#":
                visit[a][b] = 1
                q.append((a, b))


for i in range(n):
    for j in range(n):
        if migong[i][j] == "#" and visit[i][j] == 0:
            flag = True  # 设置淹没标志
            bfs(i, j)    # 搜索这个格子，看看是否需要更改淹没标志
            if flag:   # 如果淹没标志不变
                count += 1   # 被淹没的岛屿数量+1
                
print(count)
