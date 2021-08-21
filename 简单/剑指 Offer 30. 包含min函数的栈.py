"""

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)。


示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.auxiliary_stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.auxiliary_stack.append(x)
        else:
            self.stack.append(x)
            if x <= self.auxiliary_stack[-1]:
                self.auxiliary_stack.append(x)

    def pop(self):
        if self.auxiliary_stack[-1] == self.stack[-1]:
            self.auxiliary_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.auxiliary_stack[-1]
