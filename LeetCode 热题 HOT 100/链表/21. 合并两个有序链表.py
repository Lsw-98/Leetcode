# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例 1
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]

# 示例 2：
# 输入：l1 = [], l2 = []
# 输出：[]

# 示例 3：
# 输入：l1 = [], l2 = [0]
# 输出：[0]


def mergeTwoLists(self, list1, list2):
  if not list1: return list2
  if not list2: return list1

  if list1.val <= list2.val:
    list1.next = self.mergeTwoLists(list1.next, list2)
    return list1

  else:
    list2.next = self.mergeTwoLists(list1, list2.next)
    return list2
  

