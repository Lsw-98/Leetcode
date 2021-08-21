"""

有N件物品和一个最多能被重量为W 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。
每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。

输入格式
　　输入的第一行包含两个整数n, m，分别表示物品的个数和背包能装重量。
　　以后N行每行两个数Wi和Vi,表示物品的重量和价值

输出格式
　　输出1行，包含一个整数，表示最大价值。
+
"""


n, m = map(int, input().split())
weight = []
value = []
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    temp = list(map(int, input().split()))
    weight.append(temp[0])
    value.append(temp[1])

if len(weight) == 0:
    print(0)
else:
    # weight.sort()
    # value.sort()

    for j in range(1, len(weight) + 1):
        for k in range(1, m + 1):
            temp_goods = 0
            temp_not_goods = 0

            # 关键步骤，状态转移方程
            # 存放j号物品(前提是放得下j号物品)
            if k - weight[j - 1] >= 0:
                temp_goods = value[j - 1] + dp[j - 1][k - weight[j - 1]]
            # 不存放j号物品
            temp_not_goods = dp[j - 1][k]
            dp[j][k] = max(temp_goods, temp_not_goods)

print(dp[-1][-1])
