class Solution(object):
    def preorderTraversal(self, root):
        r=[]
        def preorder(node):
            if node is None:
                return
            r.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return r