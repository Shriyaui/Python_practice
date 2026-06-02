class Solution(object):
    def isValid(self, s):
        stack = []
        d = {')':'(', '}':'{', ']':'['}

        for i in s:
            if i in d.values():
                stack.append(i)
            elif not stack or stack.pop() != d[i]:
                return False

        return not stack