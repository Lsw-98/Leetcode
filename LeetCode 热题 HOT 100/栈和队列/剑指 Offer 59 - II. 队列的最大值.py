# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
# 若队列为空，pop_front 和 max_value 需要返回 - 1

# 示例 1：
# 输入:
# ["MaxQueue", "push_back", "push_back", "max_value", "pop_front", "max_value"]
# [[], [1], [2], [], [], []]
# 输出: [null, null, null, 2, 1, 2]

# 示例 2：
# 输入:
# ["MaxQueue", "pop_front", "max_value"]
# [[], [], []]
# 输出: [null, -1, -1]


from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque()

    def max_value(self):
        if self.queue:
            return max(self.queue)
        return -1

    def push_back(self, value: int):
        self.queue.append(value)

    def pop_front(self):
        if self.queue:
            return self.queue.popleft()
        return -1
