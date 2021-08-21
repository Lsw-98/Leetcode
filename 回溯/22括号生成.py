"""

数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

"""


def generateParenthesis(n):
    # 回溯
    # ans = []
    # temp = []
    #
    # def backtrace(temp, left, right):
    #     if len(temp) == 2 * n:
    #         ans.append(''.join(temp))
    #         return
    #
    #     if left < n:
    #         temp.append('(')
    #         backtrace(temp, left + 1, right)
    #         temp.pop()
    #
    #     if left > right:
    #         temp.append(')')
    #         backtrace(temp, left, right + 1)
    #         temp.pop()
    #
    # backtrace(temp, 0, 0)
    # return ans

    # 动态规划
    # dp[i]表示i组括号的所有有效组合
    # dp[i] = "(dp[p]的所有有效组合)+【dp[q]的组合】"，其中 1 + p + q = i , p从0遍历到i-1, q则相应从i-1到0

    dp = [[] for _ in range(n + 1)]  # dp[i]存放i组括号的所有有效组合
    dp[0] = [""]  # 初始化dp[0]
    for i in range(1, n + 1):  # 计算dp[i]
        for p in range(i):  # 遍历p
            l1 = dp[p]  # 得到dp[p]的所有有效组合
            l2 = dp[i - 1 - p]  # 得到dp[q]的所有有效组合
            for k1 in l1:
                for k2 in l2:
                    dp[i].append("({0}){1}".format(k1, k2))
    return dp[n]


print(generateParenthesis(3))
print(generateParenthesis(1))
print(generateParenthesis(200))
