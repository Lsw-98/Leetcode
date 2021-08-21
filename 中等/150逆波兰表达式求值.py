"""

根据 逆波兰表示法，求表达式的值。

有效的算符包括+、-、*、/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

示例1：
输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

示例2：
输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

示例3：
输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：
该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""


def evalRPN(tokens):
    num_stack = []
    for i in tokens:
        if i == '*':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(a * b)
        elif i == '/':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(int(b / a))
        elif i == '+':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(a + b)
        elif i == '-':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(b - a)
        else:
            num_stack.append(int(i))
    return num_stack[0]


print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
