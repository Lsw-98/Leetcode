"""

一个 「开心字符串」定义为：
仅包含小写字母['a', 'b', 'c'].
对所有在1到s.length - 1之间的i，满足s[i] != s[i + 1]（字符串的下标从 1 开始）。
比方说，字符串"abc"，"ac"，"b" 和"abcbabcbcb"都是开心字符串，但是"aa"，"baa"和"ababbc"都不是开心字符串。

给你两个整数 n和 k，你需要将长度为 n的所有开心字符串按字典序排序。

请你返回排序后的第 k 个开心字符串，如果长度为 n的开心字符串少于 k个，那么请你返回 空字符串。

示例 1：
输入：n = 1, k = 3
输出："c"
解释：列表 ["a", "b", "c"] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 "c" 。

示例 2：
输入：n = 1, k = 4
输出：""
解释：长度为 1 的开心字符串只有 3 个。

示例 3：
输入：n = 3, k = 9
输出："cab"
解释：长度为 3 的开心字符串总共有 12 个 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"] 。
     第 9 个字符串为 "cab"

示例 4：
输入：n = 2, k = 7
输出：""

示例 5：
输入：n = 10, k = 100
输出："abacbabacb"

"""


def getHappyString(n, k):
    ans = list()
    word = ['a', 'b', 'c']

    def backtrace(cur):
        if len(cur) == n:
            ans.append(cur[:])
            return

        for i in word:
            if len(cur) == 0:
                cur += i
                backtrace(cur)
                cur = cur[:-1]
            else:
                if cur[-1] != i:
                    cur += i
                    backtrace(cur)
                    cur = cur[:-1]

    backtrace('')
    ans.sort()
    if len(ans) < k:
        return ''
    else:
        return ans[k - 1]


# print(getHappyString(1, 3))
# print(getHappyString(1, 4))
print(getHappyString(3, 9))
print(getHappyString(2, 7))
print(getHappyString(10, 100))
