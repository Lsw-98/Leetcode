"""

给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数

"""


def maxDepth(self, root):
    if not root:
        return 0
    else:
        left_highest = self.maxDepth(root.left)
        right_highest = self.maxDepth(root.right)
        return max(left_highest, right_highest) + 1
