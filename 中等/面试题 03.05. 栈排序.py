"""

栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。
最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。
该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek返回 -1。

示例1:
输入：
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
输出：
[null,null,null,1,null,2]

示例2:
输入：
["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
[[], [], [], [1], [], []]
输出：
[null,null,null,null,null,true]

"""


class SortedStack:

    # def __init__(self):
    #     self.stack = []
    #     self.auxiliary_stack = []
    #
    # def push(self, val):
    #     if self.stack:
    #         if val <= self.stack[-1]:
    #             self.stack.append(val)
    #         else:
    #             self.auxiliary_stack.append(val)
    #             for i in range(len(self.stack) - 1, -1, -1):
    #                 self.auxiliary_stack.append(self.stack[i])
    #                 self.pop()
    #             self.auxiliary_stack.sort()
    #             for j in range(len(self.auxiliary_stack) - 1, -1, -1):
    #                 self.stack.append(self.auxiliary_stack[j])
    #                 self.auxiliary_stack.pop()
    #     else:
    #         self.stack.append(val)
    #
    # def pop(self):
    #     if self.stack:
    #         self.stack.pop()
    #
    # def peek(self):
    #     if self.stack:
    #         return self.stack[-1]
    #     else:
    #         return -1
    #
    # def isEmpty(self):
    #     return not self.stack

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, val: int) -> None:
        # 用两个while实现排序,妙啊
        while self.stack1 and self.stack1[-1] < val:
            self.stack2.append(self.stack1.pop())
        while self.stack2 and self.stack2[-1] > val:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(val)
        # 为什么我将这一步放入push()中效率就比放在peek()中慢得多
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> None:
        val = self.peek()
        if self.stack1:
            self.stack1.pop()

    def peek(self) -> int:  # 2
        if not self.stack1 and not self.stack2:
            return -1
        else:
            return self.stack1[-1]

    def isEmpty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False

    '''
    stack1 单调递减，stack2单调递增
    #1 push时，先通过两次循环保证stack1的元素都大于val，stack2的元素都小于val
    再把val加入到stack1栈顶，保证stack1+stack2是单调递减的
    #2 pop时，把stack2的元素全部pop到stack1里，整个stack1就是单调递减的，栈顶为最小元素
    '''

