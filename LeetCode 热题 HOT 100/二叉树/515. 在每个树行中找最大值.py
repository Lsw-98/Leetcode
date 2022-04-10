# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

# 示例1：
# 输入: root = [1, 3, 2, 5, 3, null, 9]
# 输出: [1, 3, 9]

# 示例2：
# 输入: root = [1, 2, 3]
# 输出: [1, 3]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def largestValues(root):
        ans = []
        if not root:
            return ans

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
            ans.append(max(result))
        return ans
