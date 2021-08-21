"""

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

"""


def isAnagram(s, t):

    # 40ms，超97%
    from collections import Counter
    # 使用Counter()函数对字符串中的字符进行计数，返回一个字典
    sdic = Counter(s)
    tdic = Counter(t)
    return sdic == tdic

    # 网上的答案，一行，实践56ms，没我的快
    # return sorted(s) == sorted(t)


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
