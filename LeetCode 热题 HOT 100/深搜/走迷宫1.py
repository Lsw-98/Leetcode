from collections import deque

n, m = map(int, input().split())
migong = []
for i in range(n):
    temp = input()
    temp = list(map(int, temp))
    migong.append(temp[:m])

g = [[""] * m for _ in range(n)]
q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    if x == n - 1 and y == m - 1:
        print(len(g[-1][-1]))
        print(g[-1][-1])
        break
    for i, j, k in [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]:
        a = x + i
        b = y + j
        if 0 <= a < n and 0 <= b < m and migong[a][b] == 0:
            migong[a][b] = 1
            q.append((a, b))
            g[a][b] = g[x][y] + k
