"""

给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"

"""


# def longestPalindrome(s):
# 超时了
# s = list(s)
# if len(s) == 1:
#     return s[0]
#
# max_len = float('-inf')
# low = -1
# high = -1
# for i in range(1, len(s) + 1):
#     for j in range(0, i):
#         temp = s[j:i]
#         if temp == temp[::-1] and i - j > max_len:
#             low = i
#             high = j
#             max_len = low - high
# return ''.join(s[high:low])


"""
基本思路
若ababa是回文串，则去掉首尾bab也一定是回文串
从短到长
"""

# 960ms
# def expandAroundCenter(s, left, right):
#     # 先有中心开始判断，然后向两边扩展
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1
#     # 这时left = -1或high = len(s)
#     # 要回退到最长子串时
#     return left + 1, right - 1
#
#
# def longestPalindrome(s):
#     start, end = 0, 0
#     for i in range(len(s)):
#         left1, right1 = expandAroundCenter(s, i, i)
#         left2, right2 = expandAroundCenter(s, i, i + 1)
#         # 记录当时最长子串的索引
#         if right1 - left1 > end - start:
#             start, end = left1, right1
#         if right2 - left2 > end - start:
#             start, end = left2, right2
#     return s[start: end + 1]


# 140ms
def longestPalindrome(s):
    left, right = 0, 0
    i = 0
    n = len(s)
    while i < n:
        low, high = i, i
        # 只有当high < n - 1时才有s[high + 1]，否则越界
        while high < n - 1 and s[i] == s[high + 1]:
            high += 1
        # 与上同理
        while low > 0 and s[i] == s[low - 1]:
            low -= 1

        # 这里要让i=high + 1，如果等于low会死循环
        # 可以换判断条件，可以改成low
        i = high + 1
        while low > 0 and high < n - 1 and s[low - 1] == s[high + 1]:
            low -= 1
            high += 1
        if high - low > right - left:
            left, right = low, high

    return s[left:right + 1]


print(longestPalindrome('bb'))
print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))
print(longestPalindrome('a'))
print(longestPalindrome('ac'))
