"""

你总共有n枚硬币，你需要将它们摆成一个阶梯形状，第k行就必须正好有k枚硬币。

给定一个数字n，找出可形成完整阶梯行的总行数。

n是一个非负整数，并且在32位有符号整型的范围内。

示例 1:
n = 5
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤
因为第三行不完整，所以返回2.

示例 2:
n = 8
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
因为第四行不完整，所以返回3.

"""


def arrangeCoins(n):
    # count = 0
    # for i in range(1, n + 1):
    #     if n - i < 0:
    #         break
    #     else:
    #         n -= i
    #         count += 1
    # return count

    # 等差数列求和
    # import math
    # return int(math.sqrt(2 * n + 0.25) - 0.5)

    # 二分法
    # 解题思路：
    # 行数和硬 币数有如下对应关系：
    # [0, 1, 2, 3, 4,......,n]
    # [0, 1, 3, 6, 10,......,((n + 1) * n) / 2]
    #
    # 我们知道n枚硬 币排列的行数不可能超过n行。
    # 所以我们从行数入手，查找硬币数。
    # 算法设计：
    # 初始化：low = 0, high = n
    # 当low <= high循环执行：
    # mid = (low + high) / 2
    # cost = (mid + 1) × mid / 2
    # 当cost==n时，说明找到了，执行return mid.
    # 当cost<n时，即排mid行用的硬币数没超过n枚，可能还能多排几行，执行low = mid + 1
    # 当cost>n时，即排mid行用的硬币数已经超过n枚，应该减少行数，执行high = mid - 1
    # 结束：返回high(为什么不是low，可以自行举例验证，比如n=8执行以上算法)
    # low = 0
    # high = n
    # while low < high:
    #     mid = (low + high) // 2
    #     count = (mid + 1) * mid / 2
    #     if count == n:
    #         return mid
    #     elif count < n:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    # return high
    left, right = 0, n
    while True:
        if left > right:
            return right
        mid = (left + right) // 2
        count = (1 + mid) * mid / 2
        if count == n:
            return mid
        elif count < n:
            left = mid + 1
        else:
            right = mid - 1


print(arrangeCoins(0))
print(arrangeCoins(1))
print(arrangeCoins(2))
print(arrangeCoins(8))
