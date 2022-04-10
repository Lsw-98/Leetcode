# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

# 说明: 叶子节点是指没有子节点的节点。

# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(root):
        res = 0
        if not root:
            return res

        def getVal(root):
            if root.left:
                points.append(root.left)
            if root.right:
                points.append(root.right)

        points = deque([root])
        while points:
            size = len(points)
            result = []
            for _ in range(size):
                temp = points.popleft()
                result.append(temp.val)
                getVal(temp)
            res += 1
        return res
