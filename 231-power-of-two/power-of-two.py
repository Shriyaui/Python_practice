import math
class Solution(object):
    def isPowerOfTwo(self, n):
        return n>0 and (math.log10(n)/math.log10(2))%1==0