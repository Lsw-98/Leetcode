"""

给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

"""


def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        return haystack.index(needle)


print(strStr("hello", "ll"))
print(strStr("aaaaa", "bba"))

