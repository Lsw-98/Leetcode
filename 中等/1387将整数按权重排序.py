"""

我们将整数 x的 权重 定义为按照下述规则将 x变成 1所需要的步数：
    1. 如果x是偶数，那么x = x / 2
    2. 如果x是奇数，那么x = 3 * x + 1
    3. 比方说，x=3 的权重为 7 。因为 3 需要 7 步变成 1 （3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）。

给你三个整数lo，hi 和k。你的任务是将区间[lo, hi]之间的整数按照它们的权重升序排，
如果大于等于 2 个整数有相同的权重，那么按照数字自身的数值升序排序。
请你返回区间[lo, hi]之间的整数按权重排序后的第k个数。
注意，题目保证对于任意整数x（lo <= x <= hi），它变成1 所需要的步数是一个 32 位有符号整数。

示例 1：
输入：lo = 12, hi = 15, k = 2
输出：13
解释：12 的权重为 9（12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）
13 的权重为 9
14 的权重为 17
15 的权重为 17
区间内的数按权重排序以后的结果为 [12,13,14,15] 。对于 k = 2 ，答案是第二个整数也就是 13 。
注意，12 和 13 有相同的权重，所以我们按照它们本身升序排序。14 和 15 同理。

示例 2：
输入：lo = 1, hi = 1, k = 1
输出：1

示例 3：
输入：lo = 7, hi = 11, k = 4
输出：7
解释：区间内整数 [7, 8, 9, 10, 11] 对应的权重为 [16, 3, 19, 6, 14] 。
按权重排序后得到的结果为 [8, 10, 11, 7, 9] 。
排序后数组中第 4 个数字为 7 。

示例 4：
输入：lo = 10, hi = 20, k = 5
输出：13

示例 5：
输入：lo = 1, hi = 1000, k = 777
输出：570

"""


# 628ms，太瓦了
# 对字典掌握太差
# 主要涉及:列表转字典，字典按value排序
def getKth(lo, hi, k):
    # initialize = list(range(lo, hi + 1))
    # weight = []
    # for i in range(lo, hi + 1):
    #     weight_count = 0
    #     while i != 1:
    #         if i & 1 == 1:
    #             i = 3 * i + 1
    #         else:
    #             i //= 2
    #         weight_count += 1
    #     weight.append(weight_count)
    # # return weight
    #
    # dict_weight = dict(zip(initialize, weight))
    # sorted_dict = sorted(dict_weight.items(), key=lambda x: x[1])
    # return sorted_dict[k - 1][0]

    # 官网的方法1:递归 992ms，内存消耗和我方法差不多，都是15MB左右
    # def getF(x):
    #     if x == 1:
    #         return 0
    #     return (getF(x * 3 + 1) if x % 2 == 1 else getF(x // 2)) + 1
    #
    # v = list(range(lo, hi + 1))
    # v.sort(key=lambda x: (getF(x), x))
    # return v[k - 1]

    # 官网的方法2:记忆法
    # 164ms，内存消耗的多:30MB
    # 基本思路:
    # 我们知道在求 f(3) 的时候会调用到 f(10)，
    # 在求 f(20) 的时候也会调用到 f(10)。
    # 同样的，如果单纯递归计算权重的话，会存在很多重复计算，
    # 我们可以用记忆化的方式来加速这个过程，
    # 即「先查表，再计算」和「先记忆，再返回」。
    # 我们可以用一个哈希映射作为这里的记忆化的「表」，这样保证每个元素的权值只被计算 1 次。
    # 在 [1, 1000]中所有 x 求 f(x) 的值的过程中，只可能出现 2228 种 x，于是效率就会大大提高。

    f = {1: 0}
    def getF(x):
        if x in f:
            return f[x]
        f[x] = (getF(x * 3 + 1) if x % 2 == 1 else getF(x // 2)) + 1
        return f[x]

    v = list(range(lo, hi + 1))
    v.sort(key=lambda x: (getF(x), x))
    return v[k - 1]


print(getKth(12, 15, 2))
print(getKth(1, 1, 1))
print(getKth(7, 11, 4))
print(getKth(10, 20, 5))
print(getKth(1, 1000, 777))
