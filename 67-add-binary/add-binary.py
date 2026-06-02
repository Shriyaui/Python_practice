class Solution(object):
    def addBinary(self, a, b):
        sum=bin(int(a,2)+int(b,2))
        return (sum[2:])