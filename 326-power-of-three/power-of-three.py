import math
class Solution(object):
    def isPowerOfThree(self, n):
        return n>0 and (math.log10(n)/math.log10(3))%1==0
        