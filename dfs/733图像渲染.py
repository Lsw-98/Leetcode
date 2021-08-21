"""

有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
给你一个坐标(sr, sc)表示图像渲染开始的像素值（行 ，列）和一个新的颜色值newColor，让你重新上色这幅图像。
从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，
接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。
将所有有记录的像素点的颜色值改为新的颜色值
最后返回经过上色渲染后的图像

示例 1:
输入:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]

1  1  1    2   2   2
1  1  0    2   2   0
1  0  1    2   0   1

解析:
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。

"""


def floodFill(image, sr, sc, newColor):
    n = len(image) - 1
    m = len(image[0]) - 1

    def dfs(x, y):
        if image[x][y] == newColor:
            return
        temp = image[x][y]
        image[x][y] = newColor

        if x == 0 and y == 0:
            if image[x][y + 1] == temp:
                dfs(x, y + 1)
            if image[x + 1][y] == temp:
                dfs(x + 1, y)

        elif x == 0 and y == m:
            if image[x][y - 1] == temp:
                dfs(x, y - 1)
            if image[x + 1][y] == temp:
                dfs(x + 1, y)

        elif x == n and y == 0:
            if image[x][y + 1] == temp:
                dfs(x, y + 1)
            if image[x - 1][y] == temp:
                dfs(x - 1, y)

        elif x == n and y == m:
            if image[x][y - 1] == temp:
                dfs(x, y - 1)
            if image[x - 1][y] == temp:
                dfs(x - 1, y)

        elif x == 0 and 0 < y < m:
            if image[x][y - 1] == temp:
                dfs(x, y - 1)
            if image[x + 1][y] == temp:
                dfs(x + 1, y)
            if image[x][y + 1] == temp:
                dfs(x, y + 1)

        elif x == n and 0 < y < m:
            if image[x][y - 1] == temp:
                dfs(x, y - 1)
            if image[x - 1][y] == temp:
                dfs(x - 1, y)
            if image[x][y + 1] == temp:
                dfs(x, y + 1)

        elif 0 < x < n and y == 0:
            if image[x - 1][y] == temp:
                dfs(x - 1, y)
            if image[x + 1][y] == temp:
                dfs(x + 1, y)
            if image[x][y + 1] == temp:
                dfs(x, y + 1)

        elif 0 < x < n and y == m:
            if image[x - 1][y] == temp:
                dfs(x - 1, y)
            if image[x + 1][y] == temp:
                dfs(x + 1, y)
            if image[x][y - 1] == temp:
                dfs(x, y - 1)

        else:
            if image[x - 1][y] == temp:
                dfs(x - 1, y)
            if image[x + 1][y] == temp:
                dfs(x + 1, y)
            if image[x][y - 1] == temp:
                dfs(x, y - 1)
            if image[x][y + 1] == temp:
                dfs(x, y + 1)

    dfs(sr, sc)
    return image


# print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
# print(floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2))
print(floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))
