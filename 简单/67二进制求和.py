"""

你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字1和0。

示例1:
输入: a = "11", b = "1"
输出: "100"

示例2:
输入: a = "1010", b = "1011"
输出: "10101"

"""


def addBinary(a, b):
    # 52ms 14.8MB
    n = list(map(int, str(int(a) + int(b))))
    n.reverse()
    for i in range(len(n)):
        if n[i] >= 2:
            if i == len(n) - 1:
                n.append(1)
                n[i] %= 2
            else:
                n[i] %= 2
                n[i + 1] += 1
    n.reverse()
    n = list(map(str, n))
    return ''.join(n)


print(addBinary("111", "1"))
print(addBinary("11", "1"))
print(addBinary("1111", "1111"))
