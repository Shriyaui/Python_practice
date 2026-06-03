class Solution(object):
    def inorderTraversal(self, root):
        r=[]
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            r.append(node.val)
            inorder(node.right)
        inorder(root)
        return r