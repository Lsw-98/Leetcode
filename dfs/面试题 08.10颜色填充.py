"""

编写函数，实现许多图片编辑软件都支持的「颜色填充」功能。
待填充的图像用二维数组 image 表示，元素为初始颜色值。初始坐标点的行坐标为 sr 列坐标为 sc。需要填充的新颜色为 newColor 。
「周围区域」是指颜色相同且在上、下、左、右四个方向上存在相连情况的若干元素。
请用新颜色填充初始坐标点的周围区域，并返回填充后的图像。

示例：
输入：
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出：[[2,2,2],[2,2,0],[2,0,1]]
解释:
初始坐标点位于图像的正中间，坐标 (sr,sc)=(1,1) 。
初始坐标点周围区域上所有符合条件的像素点的颜色都被更改成 2 。
注意，右下角的像素没有更改为 2 ，因为它不属于初始坐标点的周围区域。

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


print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
