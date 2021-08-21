"""

请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。
执行push、pop和min操作的时间复杂度必须为O(1)。

示例：

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

"""


class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.stack.append(x)
        else:
            if x < self.stack[-2]:
                self.stack.append(x)
            else:
                self.stack.append(self.stack[-2])
            self.stack.append(x)

    def pop(self):
        self.stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.stack[-2]


