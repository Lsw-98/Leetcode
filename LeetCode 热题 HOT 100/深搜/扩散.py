# 小蓝在一张无限大的特殊画布上作画。
# 这张画布可以看成一个方格图，每个格子可以用一个二维的整数坐标表示。
# 小蓝在画布上首先点了一下几个点：(0, 0), (2020, 11), (11, 14), (2000, 2000)(0, 0), (2020, 11), (11, 14), (2000, 2000)。
# 只有这几个格子上有黑色，其它位置都是白色的。

# 每过一分钟，黑色就会扩散一点。具体的，如果一个格子里面是黑色，它就会扩散到上、下、左、右四个相邻的格子中，
# 使得这四个格子也变成黑色（如果原来就是黑色，则还是黑色）。

# 请问，经过 20202020 分钟后，画布上有多少个格子是黑色的。


from collections import deque
# 将4个点存入集合和双向队列中
v = {(0, 0), (2020, 11), (11, 14), (2000, 2000)}
# 第三个参数代表经过多少分钟
q = deque([(0, 0, 0), (2020, 11, 0), (11, 14, 0), (2000, 2000, 0)])
# 初始黑格子数目
count = 4
while q:
    x, y, z = q.popleft()
    if z == 2020:
        print(count)
        break
    for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        a = x + i
        b = y + j
        if (a, b) not in v:
            v.add((a, b))
            q.append((a, b, z + 1))
            count += 1
