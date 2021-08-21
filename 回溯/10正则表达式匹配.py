"""

给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。

示例 1：
输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2:
输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。
    因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例3：
输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4：
输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5：
输入：s = "mississippi" p = "mis*is*p*."
输出：false

"""


def isMatch(s, p):
    temp = []
    p = list(p)

    def backtrace(index):
        if ''.join(temp) == s:
            return True

        for i in range(len(p)):
            if p[i] == '*':
                pass
            elif p[i] == '.':
                pass
            else:
                temp.append(p[i])

    backtrace(0)
    return False


print(isMatch("aa", "a"))
print(isMatch("aa", "a*"))
print(isMatch("ab", ".*"))
print(isMatch("aab", "c*a*b"))
print(isMatch("mississippi", "mis*is*p*."))
