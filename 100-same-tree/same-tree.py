class Solution(object):
    def isSameTree(self, p, q):
        # Both nodes are empty
        if not p and not q:
            return True

        # One is empty and the other is not
        if not p or not q:
            return False

        # Values must match
        if p.val != q.val:
            return False

        # Check left and right subtrees
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))