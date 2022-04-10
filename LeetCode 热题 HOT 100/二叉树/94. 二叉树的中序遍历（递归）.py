def inorderTraversal(root):
    res = list()

    def inorder(root):
        if not root:
            return

        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res
