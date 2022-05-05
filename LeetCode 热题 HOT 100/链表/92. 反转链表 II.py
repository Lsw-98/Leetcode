# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

# 示例 1：
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]

# 示例 2：
# 输入：head = [5], left = 1, right = 1
# 输出：[5]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(head, left, right):
        count = 0
        while count < left:
            count += 1
            head = head.next

        pre, cur = head, head

        def reList(curNode, preNode, index):
            if not cur or index == right - left:
                return pre

            res = reList(curNode.next, curNode, index + 1)
            curNode.next = preNode
            return res

        head = reList(head, None, 0)

        while head:
            head = head.next

        return head
