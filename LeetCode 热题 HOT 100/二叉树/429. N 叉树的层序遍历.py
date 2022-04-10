# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

# 树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。

# 示例 1：
# 输入：root = [1, null, 3, 2, 4, null, 5, 6]
# 输出：[[1], [3, 2, 4], [5, 6]]

# 示例 2：
# 输入：root = [1, null, 2, 3, 4, 5, null, null, 6, 7, null, 8, null, 9, 10, null, null, 11, null, 12, null, 13, null, null, 14]
# 输出：[[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


from collections import deque


class Solution:
    def levelOrder(root):
        res = []
        if not root:
            return res

        def getVal(root):
            if root.children:
                points.extend(root.children)

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
