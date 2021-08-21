"""

给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
进阶：
如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

示例 1：
输入：s = "abc", t = "ahbgdc"
输出：true

示例 2：
输入：s = "axc", t = "ahbgdc"
输出：false

"""


def isSubsequence(s, t):
    dp = [0 for _ in range(len(t))]
    temp = 0
    for i in range(len(t)):
        if temp == len(s):
            break
        if t[i] == s[temp]:
            dp[i] = s[temp]
            temp += 1
        else:
            dp[i] = s[temp]
    return temp == len(s)


print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
