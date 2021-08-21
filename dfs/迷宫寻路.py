"""


给定一个大小为N*M的迷宫，由通道('.')和墙壁('#')组成，其中通道S表示起点，通道G表示终点，
每一步移动可以达到上下左右中不是墙壁的位置。试求出起点到终点的最小步数。（本题假定迷宫是有解的）(N,M<=100)

样例输入：
10 10
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#

样例输出：
22

"""


# 本解答也输出了最短路径的轨迹(之一)
from collections import deque

MAX_VALUE = 0x7fffffff


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def bfs(maze, begin, end):
    n, m = len(maze), len(maze[0])
    dist = [[MAX_VALUE for _ in range(m)] for _ in range(n)]
    pre = [[None for _ in range(m)] for _ in range(n)]  # 当前点的上一个点,用于输出路径轨迹

    dx = [1, 0, -1, 0]  # 四个方位
    dy = [0, 1, 0, -1]
    sx, sy = begin.x, begin.y
    gx, gy = end.x, end.y

    dist[sx][sy] = 0
    queue = deque()
    queue.append(begin)
    while queue:
        curr = queue.popleft()
        find = False
        for i in range(4):
            nx, ny = curr.x + dx[i], curr.y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#' and dist[nx][ny] == MAX_VALUE:
                dist[nx][ny] = dist[curr.x][curr.y] + 1
                pre[nx][ny] = curr
                queue.append(Point(nx, ny))
                if nx == gx and ny == gy:
                    find = True
                    break
        if find:
            break
    print('最短路径的长度：')
    print(dist[gx][gy])

    print('最短路径轨迹（之一）：')
    stack = []
    curr = end
    while True:
        stack.append(curr)
        if curr.x == begin.x and curr.y == begin.y:
            break
        prev = pre[curr.x][curr.y]
        curr = prev
    while stack:
        curr = stack.pop()
        print('(%d, %d)' % (curr.x, curr.y))


if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = [['' for _ in range(m)] for _ in range(n)]
    begin = Point()
    end = Point()
    for i in range(n):
        s = input()
        maze[i] = list(s)
        if 'S' in s:
            begin.x = i
            begin.y = s.index('S')
        if 'G' in s:
            end.x = i
            end.y = s.index('G')
    bfs(maze, begin, end)
