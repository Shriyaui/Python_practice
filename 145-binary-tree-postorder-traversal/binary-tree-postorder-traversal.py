class Solution(object):
    def postorderTraversal(self, root):
        r=[]
        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            r.append(node.val)
            
        postorder(root)
        return r
        