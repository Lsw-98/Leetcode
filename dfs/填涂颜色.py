"""

题目描述
由数字0组成的方阵中，有一任意形状闭合圈，闭合圈由数字1构成，
围圈时只走上下左右4个方向。现要求把闭合圈内的所有空间都填写成2.例如：6×6的方阵（n=6），涂色前和涂色后的方阵如下：

0 0 0 0 0 0
0 0 1 1 1 1
0 1 1 0 0 1
1 1 0 0 0 1
1 0 0 0 0 1
1 1 1 1 1 1

0 0 0 0 0 0
0 0 1 1 1 1
0 1 1 2 2 1
1 1 2 2 2 1
1 2 2 2 2 1
1 1 1 1 1 1


输入格式
每组测试数据第一行一个整数n(1≤n≤30)
接下来n行，由0和1组成的n * n的方阵。
方阵内只有一个闭合圈，圈内至少有一个0

输出格式
已经填好数字2的完整方阵。

"""


"""

我们从(3, 3)这个点开始递归
用dfs(x, y)代表当前走到了(x, y)这一点
设计dfs函数
伪代码
def dfs(x, y):
    将(x, y)这一点标记为2
    枚举每一个方向
    if 这个方向可以走并且下一个方向没有走过:
        dfs(下一个方向)

"""


def dfs(x, y):
    array[x][y] = 3
    if x - 1 >= 0:
        if array[x - 1][y] == 0:
            dfs(x - 1, y)
    if x + 1 < n + 2:
        if array[x + 1][y] == 0:
            dfs(x + 1, y)
    if y - 1 >= 0:
        if array[x][y - 1] == 0:
            dfs(x, y - 1)
    if y + 1 < n + 2:
        if array[x][y + 1] == 0:
            dfs(x, y + 1)


n = int(input())
array = []
# 给外层加了一圈0
for i in range(n):
    temp = list(map(int, input().split()))
    if i == 0:
        array.append([0 for _ in range(n + 2)])
        temp.insert(0, 0)
        temp.append(0)
        array.append(temp)
    elif i == n - 1:
        temp.insert(0, 0)
        temp.append(0)
        array.append(temp)
        array.append([0 for _ in range(n + 2)])
    else:
        temp.insert(0, 0)
        temp.append(0)
        array.append(temp)

dfs(0, 0)
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == 3:
            array[i][j] = 0
        elif array[i][j] == 0:
            array[i][j] = 2

for i in range(1, len(array) - 1):
    for j in range(1, len(array[i]) - 1):
        print(array[i][j], end=' ')
    print()
