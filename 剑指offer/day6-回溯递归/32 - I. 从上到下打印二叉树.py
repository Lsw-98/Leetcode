# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7

# 返回：
# [3,9,20,15,7]


from collections import deque


def levelOrder(root):
  res = list()
  if not root: return res
  temp = deque()
  temp.append(root)
  while temp:
    node = temp.popleft()
    res.append(node.val)
    if node.left: temp.append(node.left)
    if node.right: temp.append(node.right)
  return res