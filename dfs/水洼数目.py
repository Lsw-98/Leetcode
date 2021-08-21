"""

有一个大小为 N*M 的园子，雨后积起了水。八连通的积水被认为是连接在一起的。请求出园子里总共有多少水洼？（八连通指的是下图中相对 W 的*的部分）

n = 10, m = 12

W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.

"""


n, m = map(int, input().split())
shuiwa = []
for i in range(n):
    temp = list(map(str, input()))
    shuiwa.append(temp)
ans = 0


def dfs(x, y):
    shuiwa[x][y] = '.'
    if x - 1 >= 0 and shuiwa[x - 1][y] == 'W':
        dfs(x - 1, y)
    if x + 1 < n and shuiwa[x + 1][y] == 'W':
        dfs(x + 1, y)
    if y - 1 >= 0 and shuiwa[x][y - 1] == 'W':
        dfs(x, y - 1)
    if y + 1 < m and shuiwa[x][y + 1] == 'W':
        dfs(x, y + 1)
    if x - 1 >= 0 and y - 1 >= 0 and shuiwa[x - 1][y - 1] == 'W':
        dfs(x - 1, y - 1)
    if x - 1 >= 0 and y + 1 < m and shuiwa[x - 1][y + 1] == 'W':
        dfs(x - 1, y + 1)
    if x + 1 < n and y - 1 >= 0 and shuiwa[x + 1][y - 1] == 'W':
        dfs(x + 1, y - 1)
    if x + 1 < n and y + 1 < m and shuiwa[x + 1][y + 1] == 'W':
        dfs(x + 1, y + 1)


for i in range(n):
    for j in range(m):
        if shuiwa[i][j] == 'W':
            dfs(i, j)
            ans += 1
print(ans)
