# 请实现一个函数按照之字形顺序打印二叉树，
# 即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
#   [20,9],
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
  index = 1

  while temp:
    node = temp.popleft()
    lst.append(node.val)
            
    if node.left: mid.append(node.left)
    if node.right: mid.append(node.right)

    if not temp:
      if index % 2 == 0:
        res.append(lst[::-1])
      else:
        res.append(lst[:])
      lst.clear()
      temp = mid
      mid = deque()
      index += 1
    return res