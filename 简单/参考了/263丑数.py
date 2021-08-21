"""

编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数2, 3, 5的正整数。

示例 1:
输入: 6
输出: true
解释: 6 = 2 ×3

示例 2:
输入: 8
输出: true
解释: 8 = 2 × 2 ×2

示例3:
输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数7。

说明：
1是丑数。
输入不会超过 32 位有符号整数的范围:[−2 ** 31, 2 ** 31− 1]。

"""


def isUgly(num):
    if num <= 0:
        return False
    else:
        while num % 5 == 0:
            num /= 5
        while num % 3 == 0:
            num /= 3
        while num % 2 == 0:
            num /= 2
        return num == 1


print(isUgly(1))
print(isUgly(6))
print(isUgly(8))
print(isUgly(14))
