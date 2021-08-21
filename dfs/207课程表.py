"""

你这个学期必须选修 numCourses 门课程，记为0到numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组prerequisites 给出，
其中prerequisites[i] = [ai, bi] ，表示如果要学习课程ai 则 必须 先学习课程bi 。

例如，先修课程对[0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false

示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

示例 2：
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

"""


# 判断是否是有向无环图
def canFinish(numCourses, prerequisites):
    temp = []
    for i in range(len(prerequisites)):
        for j in range(len(prerequisites[i])):
            temp.append(prerequisites[i][j])
    temp.sort()
    tu = [temp[0]]
    for i in range(1, len(temp)):
        if temp[i] != temp[i - 1]:
            tu.append(temp[i])
    n = len(tu)
    tuarray = [[0] * n for _ in range(n)]

    for i in range(len(prerequisites)):
        a = prerequisites[i][0]
        b = prerequisites[i][1]
        tuarray[a][b] = 1


print(canFinish(2, [[1, 0]]))
print(canFinish(2, [[1, 0], [0, 1]]))
