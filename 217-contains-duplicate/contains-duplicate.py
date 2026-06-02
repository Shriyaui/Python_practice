class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()  # O(n log n)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False