# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明：叶子节点是指没有子节点的节点。

# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2

# 示例 2：
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(root):
        res = 0
        if not root:
            return res

        def getVal(root):
            if root.left:
                points.append(root.left)
            if root.right:
                points.append(root.right)

        flag = True
        points = deque([root])
        while points:
            size = len(points)
            result = []
            for _ in range(size):
                temp = points.popleft()
                if not temp.left and not temp.right:
                    flag = False
                    break
                result.append(temp.val)
                getVal(temp)
            res += 1
            if not flag:
                break
        return res
