"""

给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:
输入：s = "bcabc"
输出："abc"

示例 2：
输入：s = "cbacdcbc"
输出："acdb"

"""


def removeDuplicateLetters(s):
    min_index = min(s).index
    return min_index



print(removeDuplicateLetters("bcabc"))
print(removeDuplicateLetters("cbacdcbc"))
