# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

# 示例 1：
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]

# 示例 2：
# 输入：root = []
# 输出：[]

# 示例 3：
# 输入：root = [1]
# 输出：[1]


def postorderTraversal(root):
  res = list()

  def postorder(root):
    if not root:
      return 

    postorder(root.left)
    postorder(root.right)
    res.append(root.val)
    
  postorder(root)
  return res
