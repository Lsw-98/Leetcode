"""

你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通队列的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

注意：

你只能使用队列的基本操作 —— 也就是push to back、peek/pop from front、size 和is empty这些操作。
你所使用的语言也许不支持队列。你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列, 只要是标准的队列操作即可。

示例：
输入：
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 2, 2, false]

解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False

"""


class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        self.queue1.reverse()
        for i in range(len(self.queue1) - 1, -1, -1):
            self.queue2.append(self.queue1[i])
            self.queue1.pop()
        self.queue2.reverse()
        for j in range(len(self.queue2) - 1, 0, -1):
            self.queue1.append(self.queue2[j])
            self.queue2.pop()
        return self.queue2.pop()

    def top(self):
        return self.queue1[-1]

    def empty(self):
        return len(self.queue1) == 0


ms = MyStack()
ms.push(1)
ms.push(2)
print(ms.top())
print(ms.pop())
print(ms.empty())
