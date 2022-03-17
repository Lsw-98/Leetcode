# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。

# 示例 1：
# 输入：s = "()"
# 输出：true

# 示例 2：
# 输入：s = "()[]{}"
# 输出：true

# 示例 3：
# 输入：s = "(]"
# 输出：false

# 示例 4：
# 输入：s = "([)]"
# 输出：false

# 示例 5：
# 输入：s = "{[]}"
# 输出：true


def isValid(s):
  left_stack = list()
  const = ["(", "{", "["]
  kuohao = [["(", ")"], ["{", "}"], ["[", "]"]]
  for i in s:
    if i in const:
      left_stack.append(i)
    else:
      for j in range(len(kuohao)):
        if kuohao[j][1] == i:
          if len(left_stack) > 0 and kuohao[j][0] == left_stack[-1]:
            left_stack.pop()
          else:
            return False
  if left_stack:
    return False
  else:
    return True
  

print(isValid("("))
# print(isValid("()"))
# print(isValid("()[]{}"))
# print(isValid("(]"))
# print(isValid("([)]"))
# print(isValid("{[]}"))
