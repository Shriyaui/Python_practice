class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        return len(words[-1]) if words else 0
        