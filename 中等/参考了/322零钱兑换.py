"""

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回-1。

你可以认为每种硬币的数量是无限的。

示例1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2

"""


# 最大最小值动态规划问题(求最值形的的动态规划)
# 基本思路: 最优策略肯定是有k枚硬币a1, a2, ..., ak的面值和为amount
# 所以一定有最后一枚硬币ak, 除掉这枚硬币, 前面的硬币面值为amount - ak
# 设置一个列表将1~amount的值记录下来，不需要递归重复计算
# 如果f[j - coins[k]] > 0, 则f[j] += 1, 代表coins[k]用过一次
# 如此循环，f[amount]的值便是使用的最少硬币数
# 2360ms 超时了啊
# def coinChange(coins, amount):
#     f = [float('inf') for i in range(amount + 1)]
#     f[0] = 0
#     for j in range(1, amount + 1):
#         for k in range(len(coins)):
#             if (j >= coins[k]) and (f[j - coins[k]] != float('inf')):
#                 # f[j] = f[j - coins[k]] + 1
#                 f[j] = min(f[j - coins[k]] + 1, f[j])
#     if f[amount] == float('inf'):
#         f[amount] = -1
#     return f[-1]


# 76ms
def coinChange(coins, amount):
    import math
    if amount == 0:
        return 0
    n = len(coins)
    if n == 0:
        return -1

    # 先把硬币排序, 由大到小
    coins.sort(reverse=True)

    res = float('inf')

    def helper(count, amount, index):
        """
        :param count: 当前使用的硬币数
        :param amount: 剩余钱数
        :param index: 使用第几个硬币
        :return:
        """
        # nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
        nonlocal res, n

        if amount == 0:
            res = min(res, count)
            return
        if index == n:
            return
        coin = coins[index]
        # math.ceil()向上取整函数
        if math.ceil(amount / coin) + count >= res:
            return

        for i in range(amount // coin, -1, -1):
            helper(count + i, amount - coin * i, index + 1)

    helper(0, amount, 0)

    return -1 if res == float('inf') else res


print(coinChange([2, 5, 7], 27))
print(coinChange([1, 2, 5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1], 1))
print(coinChange([1], 2))
