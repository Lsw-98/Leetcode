"""

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例1:
输入: 1
输出: true
解释: 2 ** 0 = 1

示例 2:
输入: 16
输出: true
解释: 2 ** 4 = 16

示例 3:
输入: 218
输出: false

"""


def isPowerOfTwo(n):
    # 如果一个数n是2的幂，则其只有首位为1，其后若干个0，必然有n & (n - 1)为0。
    # 因此，判断一个数n是否为2的幂，只需要判断n&(n-1)是否为0即可。
    return n > 0 and n & (n - 1) == 0


print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(218))
print(isPowerOfTwo(1000))  # 232
