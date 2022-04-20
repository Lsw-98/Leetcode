# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isSymmetric(root):
        if not root:
            return True

        points = deque([root])
        while points:
            res = []
            size = len(points)
            for _ in range(size):
                temp = points.popleft()
                if temp == -999:
                    res.append(-999)
                else:
                    res.append(temp.val)
                    if temp.left:
                        points.append(temp.left)
                    else:
                        points.append(-999)
                    if temp.right:
                        points.append(temp.right)
                    else:
                        points.append(-999)
            if res != res[::-1]:
                return False
        return True
