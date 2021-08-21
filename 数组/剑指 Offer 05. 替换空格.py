"""

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

"""


def replaceSpace(s):
    temp = "%20"
    s = list(s)
    n = len(s)
    for i in range(n):
        if s[i] == " ":
            s[i] = temp
    return ''.join(s)


print(replaceSpace("We are happy."))
