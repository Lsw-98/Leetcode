"""
其实我们在学习图论或者图相关的算法的时候会遇到两个基本的算法，
深度优先遍历和广度优先遍历，
在树中，前序遍历类似于深度优先遍历，后序遍历类似于广度优先遍历，
而一般通常使用栈来实现深度，队列实现广度。
"""


class Node(object):
    """ 节点类 """

    def __init__(self, val=-1):
        self.val = val  # 是节点的data,如果是-1表示为空节点
        self.lChild = None
        self.rChild = None


class Tree(object):
    """ 树类 """

    def __init__(self):
        self.root = Node()
        self.Queue = []

    def add(self, val):
        """ 为树添加节点 是按照层次遍历来插入的，队列中的是子节点没有满的节点的层次遍历 """
        node = Node(val)
        # 如果树是空的，则对根节点赋值，赋值之后树一直不为空
        if self.root.val == -1:
            self.root = node
            self.Queue.append(self.root)
        else:
            """
            此节点的子树没有齐，在此节点上插入左右子节点
            """
            tree_node = self.Queue[0]
            if not tree_node.lChild:
                tree_node.lChild = node
                self.Queue.append(tree_node.lChild)
            elif not tree_node.rChild:
                tree_node.rChild = node
                self.Queue.append(tree_node.rChild)
                # 删除已经有左右子节点的节点
                self.Queue.pop(0)

    def preorder_recursive(self, root):
        """ 利用递归的先序遍历 根左右"""
        if root:
            print(root.val, end=' ')
            self.preorder_recursive(root.lChild)
            self.preorder_recursive(root.rChild)

    def miorder_recursive(self, root):
        """ 利用递归的中序遍历 左根右 """
        if root:
            self.miorder_recursive(root.lChild)
            print(root.val, end=' ')
            self.miorder_recursive(root.rChild)

    def laterorder_recursive(self, root):
        """ 利用递归的后序遍历 左右根 """
        if root:
            self.laterorder_recursive(root.lChild)
            self.laterorder_recursive(root.rChild)
            print(root.val, end=' ')

    def preorder_stack(self, root):
        """ 利用堆栈实现先序遍历 """
        if not root:
            return
        Stack = []
        node = root
        while node or Stack:
            while node:
                print(node.val, end=' ')
                Stack.append(node)  # 将沿途的最左节点打印出来并按顺序入队
                node = node.lChild
            node = Stack.pop()
            node = node.rChild  # 将根左的左右节点重新来进行先序遍历，同时队列不断加入最左节点

    def miorder_stack(self, root):
        """ 利用堆栈实现中序遍历 """
        if not root:
            return
        Stack = []
        node = root
        while node or Stack:
            while node:
                Stack.append(node)
                node = node.lChild
            node = Stack.pop()
            print(node.val, end=' ')
            node = node.rChild

    def laterorder_stack(self, root):
        """
        利用两个栈实现后序遍历 左右根
        """

        if not root:
            return
        Stack1 = []
        Stack2 = []
        node = root
        Stack1.append(node)
        while Stack1:
            node = Stack1.pop()  # 弹出顺序是根右左
            if node.lChild:
                Stack1.append(node.lChild)  # 加入顺序是左右，弹出顺序就是右左
            if node.rChild:
                Stack1.append(node.rChild)
            Stack2.append(node)  # 与Stack1弹出顺序一致

        while Stack2:
            print(Stack2.pop().val, end=' ')

    def level_queue(self, root):
        """
        利用队列实现层次遍历
        """
        if not root:
            return
        Queue = []
        node = root
        Queue.append(node)
        while Queue:
            # 先进先出，pop第一个元素，pop默认是弹出最后一个元素
            node = Queue.pop(0)
            print(node.val, end=' ')
            if node.lChild:
                Queue.append(node.lChild)
            if node.rChild:
                Queue.append(node.rChild)


if __name__ == '__main__':
    """主函数"""
    elems = range(1, 11)  # 生成十个数据作为树节点
    tree = Tree()  # 新建一个树对象
    for elem in elems:
        tree.add(elem)  # 逐个添加树的节点

    print('\n队列实现层次遍历:', tree.level_queue(tree.root))

    print('\n递归实现先序遍历:', tree.preorder_recursive(tree.root))

    print('\n递归实现中序遍历:', tree.miorder_recursive(tree.root))

    print('\n递归实现后序遍历:', tree.laterorder_recursive(tree.root))

    print('\n堆栈实现先序遍历:', tree.preorder_stack(tree.root))

    print('\n堆栈实现中序遍历:', tree.miorder_stack(tree.root))

    print('\n堆栈实现后序遍历:', tree.laterorder_stack(tree.root))

