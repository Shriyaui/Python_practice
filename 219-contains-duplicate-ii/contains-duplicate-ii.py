class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for idx, val in enumerate(nums):
            if val in seen and idx - seen[val] <= k:
                return True
            seen[val] = idx
        return False