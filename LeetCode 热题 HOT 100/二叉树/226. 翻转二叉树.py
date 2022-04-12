# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

# 示例 1：
# 输入：root = [4, 2, 7, 1, 3, 6, 9]
# 输出：[4, 7, 2, 9, 6, 3, 1]

# 示例 2：
# 输入：root = [2, 1, 3]
# 输出：[2, 3, 1]

# 示例 3：
# 输入：root = []
# 输出：[]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def invertTree(self, root):
        if not root:
            return None

        points = deque([root])
        while points:
            size = len(points)
            for _ in range(size):
                temp = points.popleft()
                if temp.left:
                    points.append(temp.left)
                if temp.right:
                    points.append(temp.right)
                temp.left, temp.right = temp.right, temp.left
        return root
