"""

给定两个整数，被除数dividend和除数divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数dividend除以除数divisor得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例1:
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例2:
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2

"""


def divide(dividend, divisor):
    MIN_INT, MAX_INT = -2147483648, 2147483647  # [−2**31, 2**31−1]
    flag = 1  # 存储正负号，并将分子分母转化为正数
    if dividend < 0:
        flag, dividend = -flag, -dividend
    if divisor < 0:
        flag, divisor = -flag, -divisor

    res = 0
    while dividend >= divisor:  # 例：1023 / 1 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 1
        cur = divisor
        multiple = 1
        while cur + cur < dividend:  # 用加法求出保证divisor * multiple <= dividend的最大multiple
            cur += cur  # 即cur分别乘以1, 2, 4, 8, 16...2^n，即二进制搜索
            multiple += multiple
        dividend -= cur
        res += multiple

    res = res if flag > 0 else -res  # 恢复正负号

    if res < MIN_INT:  # 根据是否溢出返回结果
        return MIN_INT
    elif MIN_INT <= res <= MAX_INT:
        return res
    else:
        return MAX_INT


print(divide(10, 3))
print(divide(7, -3))
print(divide(-1, -1))
