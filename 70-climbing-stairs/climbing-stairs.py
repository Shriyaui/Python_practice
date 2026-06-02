class Solution(object):
    def climbStairs(self, n):
        s = [1, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
               s[i] = s[i - 1] + s[i - 2]
        return s[n]
        