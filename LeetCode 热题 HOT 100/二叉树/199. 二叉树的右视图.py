# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# 示例 1:
# 输入: [1, 2, 3, null, 5, null, 4]
# 输出: [1, 3, 4]

# 示例 2:
# 输入: [1, null, 3]
# 输出: [1, 3]

# 示例 3:
# 输入: []
# 输出: []


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def rightSideView(root):
        ans = []
        if not root:
            return ans
        res = []

        def getVal(node):
            if node.left:
                points.append(node.left)
            if node.right:
                points.append(node.right)

        points = deque([root])
        while points:
            result = []
            size = len(points)
            for _ in range(size):
                temp = points.popleft()
                result.append(temp.val)
                getVal(temp)
            res.append(result)

        for i in range(len(res)):
            ans.append(res[i][-1])
        return ans
