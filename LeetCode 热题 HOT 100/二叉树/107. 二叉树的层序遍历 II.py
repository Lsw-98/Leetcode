# 给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# 示例 1：
# 输入：root = [3, 9, 20, null, null, 15, 7]
# 输出：[[15, 7], [9, 20], [3]]

# 示例 2：
# 输入：root = [1]
# 输出：[[1]]

# 示例 3：
# 输入：root = []
# 输出：[]


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def levelOrderBottom(root):
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
            res.append(result)
        res.reverse()
        return res
