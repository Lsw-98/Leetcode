"""

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

"""


def reverse(x):
    if x < 0:
        x *= -1
        strx = str(x)
        reverse_strx = int(strx[::-1])
        if -2 ** 31 > reverse_strx or reverse_strx > 2 ** 31 - 1:
            return 0
        else:
            return -1 * reverse_strx
    else:
        strx = str(x)
        reverse_strx = int(strx[::-1])
        if -2 ** 31 > reverse_strx or reverse_strx > 2 ** 31 - 1:
            return 0
        else:
            return reverse_strx


print(reverse(120))
