# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：

# [
#   [3],
#   [9,20],
#   [15,7]
# ]


from collections import deque


def levelOrder(root):
  res = list()
  if not root: return res
  temp = deque()
  temp.append(root)
  mid = deque()
  lst = list()
  while temp:
    node = temp.popleft()
    lst.append(node.val)
      
    if node.left: mid.append(node.left)
    if node.right: mid.append(node.right)

    if not temp:
      res.append(lst[:])
      lst.clear()
      temp = mid
      mid = deque()
  return res
