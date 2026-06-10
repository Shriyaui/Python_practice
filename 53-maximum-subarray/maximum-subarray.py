class Solution(object):
    def maxSubArray(self, nums):
        max_sum = curr = nums[0]
        for num in nums[1:]:
            curr = max(num, curr + num)
            max_sum = max(max_sum, curr)
        return max_sum
        