class Solution(object):
    def isBalanced(self, root):

        def dfs(root):
            if not root:
                return [True, 0]

            leftBalanced, leftHeight = dfs(root.left)
            rightBalanced, rightHeight = dfs(root.right)

            balanced = (
                leftBalanced and
                rightBalanced and
                abs(leftHeight - rightHeight) <= 1
            )

            height = 1 + max(leftHeight, rightHeight)

            return [balanced, height]

        return dfs(root)[0]
        