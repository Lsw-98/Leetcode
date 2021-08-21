"""

给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:
输入: 3
输出: 0
解释:3! = 6, 尾数中没有零。

示例2:
输入: 5
输出: 1
解释:5! = 120, 尾数中有 1 个零.

"""


def trailingZeroes(n):
    # import math
    # fac = list(map(int, str(math.factorial(n))))
    # count = 0
    # for i in fac[::-1]:
    #     if i == 0:
    #         count += 1
    #     else:
    #         break
    # return count

    # import math
    # fac = math.factorial(n)
    # count = 0
    # while fac != 0:
    #     if fac % 10 != 0:
    #         return count
    #     else:
    #         fac //= 10
    #         count += 1
    # return count

    # 2 * 5 = 10 所以只要计算阶乘中 2和5的对数，但2一定比5多，因为经过xx5之前都会经过xx2，xx4，
    # 这些分解下来都有2的因子，所以只需计算因子5的个数，5到25之间有10，15，20，25，
    # 这5个5的倍数，0到5之间有5这1个5的倍数。25的阶乘中5的因子个数是6个。
    count = 0
    while n >= 5:
        count += 1
        n //= 5
    return count


print(trailingZeroes(3))
print(trailingZeroes(5))
print(trailingZeroes(7))

