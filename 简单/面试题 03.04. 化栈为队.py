"""

实现一个MyQueue类，该类用两个栈来实现一个队列。

示例：
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

"""


class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self) -> int:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        temp = self.out_stack.pop()
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
        return temp

    def peek(self):
        return self.in_stack[0]

    def empty(self) -> bool:
        return not self.in_stack

