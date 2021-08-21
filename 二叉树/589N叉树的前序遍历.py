"""

给定一个 N 叉树，返回其节点值的 前序遍历 。

N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔。

"""


def preorder(self, root: 'Node') -> List[int]:
    stack = [root]
    output = []
    while stack:
        root = stack.pop()
        output.append(root.val)
        stack.extend(root.children[::-1])
    return output
