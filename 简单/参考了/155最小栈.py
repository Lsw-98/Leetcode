"""

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop()—— 删除栈顶的元素。
top()—— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。


示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

"""


class MinStack:

    # 方法一 辅助栈
    # 64ms
    # 基本思路:
    # 当一个元素要入栈时，我们取当前辅助栈的栈顶存储的最小值，与当前元素比较得出最小值，将这个最小值插入辅助栈中；
    # 当一个元素要出栈时，我们把辅助栈的栈顶元素也一并弹出；
    # 在任意一个时刻，栈内元素的最小值就存储在辅助栈的栈顶元素中。
    def __init__(self):
        import math
        # 数据栈
        self.stack = []
        # 辅助栈
        # math.inf常量是在math模块中定义的预定义常量，它返回浮点正无穷大(等效于float('inf'))
        self.min_stack = [math.inf]

    def push(self, x):
        self.stack.append(x)
        if x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

    # 方法二 在栈中多添加一组min_ele
