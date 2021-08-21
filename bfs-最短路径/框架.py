# bfs主要用来解决最短路径问题
from collections import deque
fangxiang = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(start, target):
    q = deque()  # 核心数据结构
    visited = []  # 标记走过的点，避免走回头路
    q.append(start)
    visited.append(start)
    step = 0  # 记录步数

    while q:
        n = len(q)

        # 将当前队列中的所有结点向四周扩散
        for i in range(n):
            temp = q.popleft()  # 将队头出栈

            if temp == target:
                return step

            # 将temp相邻节点入队
            for j in range(len(fangxiang)):
                if 0 <= x + fangxiang[j][0] < 行 and 0 <= y + fangxiang[j][1] < 列:

                    if 该点 not in visited:
                        q.append(该点)
                        visited.append(该点)

        step += 1