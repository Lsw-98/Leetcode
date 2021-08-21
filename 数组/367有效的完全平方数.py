"""

给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

示例 1：
输入：num = 16
输出：true

示例 2：
输入：num = 14
输出：false

"""


def isPerfectSquare(num):
    if num == 1:
        return True
    low = 2
    high = num // 2 + 1
    while low < high:
        x = low + (high - low) // 2
        temp = x * x
        if temp == num:
            return True
        elif temp > num:
            high -= 1
        else:
            low += 1
    return False


print(isPerfectSquare(9))
# print(isPerfectSquare(4))
# print(isPerfectSquare(16))
# print(isPerfectSquare(14))
