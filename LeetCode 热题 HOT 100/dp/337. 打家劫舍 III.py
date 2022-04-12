# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

# 示例 1:
# 输入: root = [3, 2, 3, null, 3, null, 1]
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

# 示例 2:
# 输入: root = [3, 4, 5, 1, 3, null, 1]
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9


# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generate_tree(vais):
        if len(vais) == 0:
            return None
        que = []
        fill_left = True
        for val in vais:
            node = TreeNode(val) if val else None
        if len(que) == 0:
            root = node
            que.append(node)
        elif fill_left:
            que[0].left = node
            fill_left = False
            if node:
                que.append(node)
        else:
            que[0].right = node
            if node:
                que.append(node)
            que.pop(0)
            fill_left = True
        return root

    def rob(self, root):
        res = 0
        even = []   # 偶数层
        odd = []    # 奇数层
        if not root:
            return res

        def getVal(root):
            if root.left:
                points.append(root.left)
            if root.right:
                points.append(root.right)

        points = deque([root])
        flag = True    # 奇数
        while points:
            size = len(points)
            result = []
            for _ in range(size):
                temp = points.popleft()
                result.append(temp.val)
                getVal(temp)
            if flag:
                odd.append(sum(result))
            else:
                even.append(sum(result))
            flag = ~flag
        return max(sum(odd), sum(even))


s = Solution()
t = [3, 2, 3, None, 3, None, 1]
res = s.generate_tree(s.rob(t))
print(res)
