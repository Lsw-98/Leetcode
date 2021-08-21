"""

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

"""


def addStrings(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return str(num1 + num2)


print(addStrings("231", "12"))
