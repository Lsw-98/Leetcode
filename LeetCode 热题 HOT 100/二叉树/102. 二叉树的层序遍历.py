# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(root):
        res = []
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
            res.append(result)
        return res
