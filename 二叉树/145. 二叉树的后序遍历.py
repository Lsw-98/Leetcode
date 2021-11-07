 def postorderTraversal(self, root):
   res = list()
   
   def postorder(root):
     if not root:
       return
     
     postorder(root.left)
     postorder(root.right)
     res.append(root.val)
   postorder(root)
   return res