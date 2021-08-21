"""

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：

输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]

"""


class ListNode:
    def __init__(self, item=0, next=None):
        self.item = item
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2  # 终止条件，直到两个链表都空
        if not l2:
            return l1
        if l1.item <= l2.item:  # 递归调用
            l1, l2 = l2, l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


s = Solution()
# print(s.mergeTwoLists([1, 2, 3, 4], [1, 4, 5]))
