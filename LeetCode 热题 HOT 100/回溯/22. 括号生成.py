# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

# 示例 1：
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]

# 示例 2：
# 输入：n = 1
# 输出：["()"]


def generateParenthesis(n):
    res = list()
    temp = list()

    def backtrace(left, right):
        if len(temp) == n * 2:
            res.append(''.join(temp[:]))
            return

        if left < n:
            temp.append("(")
            left += 1
            backtrace(left, right)
            left -= 1
            temp.pop()

        if right < left:
            temp.append(")")
            right += 1
            backtrace(left, right)
            right -= 1
            temp.pop()

    backtrace(0, 0)
    return res


print(generateParenthesis(3))
print(generateParenthesis(1))
