"""

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

"""


class CQueue:

    # 1804ms
    # def __init__(self):
    #     self.stack1 = []
    #     self.stack2 = []
    #
    # def appendTail(self, value):
    #     self.stack1.append(value)
    #
    # def deleteHead(self) -> int:
    #     if len(self.stack1) == 0:
    #         return -1
    #     else:
    #         for i in range(len(self.stack1) - 1, 0, -1):
    #             self.stack2.append(self.stack1.pop())
    #         res = self.stack1.pop()
    #         for j in range(len(self.stack2) - 1, -1, -1):
    #             self.stack1.append(self.stack2.pop())
    #     return res

    # 372ms
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, value: int) -> None:
        self.in_stack.append(value)

    def deleteHead(self) -> int:
        if len(self.out_stack) > 0:
            return self.out_stack.pop()
        elif len(self.in_stack) > 0:
            self.out_stack = self.in_stack[::-1]
            # 将列表清空？
            self.in_stack.clear()
            return self.out_stack.pop()
        else:
            return -1
