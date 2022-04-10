# 给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10 ** -5 以内的答案可以被接受。

# 示例 1：
# 输入：root = [3, 9, 20, null, null, 15, 7]
# 输出：[3.00000, 14.50000, 11.00000]
# 解释：第 0 层的平均值为 3, 第 1 层的平均值为 14.5, 第 2 层的平均值为 11 。
# 因此返回[3, 14.5, 11] 。

# 示例 2:
# 输入：root = [3, 9, 20, 15, 7]
# 输出：[3.00000, 14.50000, 11.00000]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def averageOfLevels(root):
        res = []
        if not root:
            return res

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
            res.append(sum(result) / len(result))
        return res
