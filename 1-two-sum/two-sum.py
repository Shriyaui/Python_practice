class Solution(object):
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            n = target - nums[i]

            if n in d:
                return [d[n], i]

            d[nums[i]] = i