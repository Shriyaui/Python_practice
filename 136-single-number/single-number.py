class Solution(object):
    def singleNumber(self, nums):
        result = 0
        
        # Go through each number in the array
        for num in nums:
            result = result ^ num  # XOR operation
        
        # After the loop, result contains the single number
        return result