"""

给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：
    1.左括号必须用相同类型的右括号闭合。
    2.左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true

示例3：
输入：s = "(]"
输出：false

示例4：
输入：s = "([)]"
输出：false

示例5：
输入：s = "{[]}"
输出：true

"""


def isValid(s):
    # 用栈
    brackets_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    brackets_list = []
    for i in range(len(s)):
        if s[i] in brackets_dict.keys():
            brackets_list.append(s[i])
        else:
            if len(brackets_list) > 0 and brackets_list[-1] == list(brackets_dict.keys())[list(brackets_dict.values()).index(s[i])]:
                brackets_list.pop()
            else:
                return False
    if len(brackets_list) == 0:
        return True
    else:
        return False


print(isValid(']'))
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
