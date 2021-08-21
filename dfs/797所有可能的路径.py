"""

给一个有n个结点的有向无环图，找到所有从0到n-1的路径并输出（不要求按顺序）

二维数组的第 i 个数组中的单元都表示有向图中 i 号结点所能到达的下一些结点
(有向图是有方向的，即规定了 a→b 你就不能从 b→a)空就是没有下一个结点了。

示例 1：
输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3

示例 2：
输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

示例 3：
输入：graph = [[1],[]]
输出：[[0,1]]

示例 4：
输入：graph = [[1,2,3],[2],[3],[]]
输出：[[0,1,2,3],[0,2,3],[0,3]]

示例 5：
输入：graph = [[1,3],[2],[3],[]]
输出：[[0,1,2,3],[0,3]]

"""


def allPathsSourceTarget(graph):
    array = [[0] * len(graph) for _ in range(len(graph))]
    i = 0
    for j in range(len(graph)):
        for k in range(len(graph[j])):
            array[i][graph[j][k]] = 1
        i += 1

    


print(allPathsSourceTarget([[1, 2], [3], [3], []]))
print(allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
print(allPathsSourceTarget([[1], []]))
print(allPathsSourceTarget([[1, 2, 3], [2], [3], []]))
print(allPathsSourceTarget([[1, 3], [2], [3], []]))
