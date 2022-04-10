def postorderTraversal(root):
    res = []

    def getVal(root):
        if root:
            getVal(root.left)
            getVal(root.right)
            res.append(root.val)

    getVal(root)
    return res
