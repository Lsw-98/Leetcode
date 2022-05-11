# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 1

        def backtrace(node):
            if not node:
                return 0

            left = backtrace(node.left)
            right = backtrace(node.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1
        backtrace(root)
        return self.ans - 1
