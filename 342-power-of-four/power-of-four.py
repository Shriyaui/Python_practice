import math
class Solution(object):
    def isPowerOfFour(self, n):
        return n>0 and (math.log10(n)/math.log10(4))%1==0
        