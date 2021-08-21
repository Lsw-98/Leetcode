"""

给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

示例1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
 请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0

"""


def lengthOfLongestSubstring(s):
    ans = 0
    n = len(s)
    start = 0
    end = 0
    temp = []
    while end < n:
        if s[end] not in temp:
            temp.append(s[end])
            end += 1
            ans = max(ans, len(s[start:end]))
        else:
            while s[start] != s[end]:
                temp.remove(s[start])
                start += 1
            temp.remove(s[start])
            start += 1

    return ans


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("abbcdef"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("dvdf"))
print(lengthOfLongestSubstring("dvxcdf"))
