"""

统计所有小于非负整数n的质数的数量。

示例 1：
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

示例 2：
输入：n = 0
输出：0

示例 3：
输入：n = 1
输出：0

提示：
0 <= n <= 5 * 106

"""


def countPrimes(n):
    if n < 3:
        return 0
    else:
        # 首先生成了一个全部为1的列表
        output = [1] * n

        # 因为0和1不是质数,所以列表的前两个位置赋值为0
        output[0], output[1] = 0, 0

        # 从index = 2开始遍历,output[2]==1,即表明第一个质数为2,然后将2的倍数对应的索引全部赋值为0.
        # 此时output[3] == 1,即表明下一个质数为3,同样划去3的倍数.以此类推.
        for i in range(2, int(n ** 0.5) + 1):
            if output[i] == 1:
                # 从 i * i开始到n， 步长为n
                output[i * i:n:i] = [0] * len(output[i * i:n:i])
    # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
    return sum(output)


print(countPrimes(10))
print(countPrimes(0))
print(countPrimes(1))
