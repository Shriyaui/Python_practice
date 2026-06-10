class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        # Start from index 2 (third element)
        index = 2
        
        for i in range(2, len(nums)):
            # Check if current number is different from the number two positions back
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1
        
        return index


# Alternative solution with more explicit logic
class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        index = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1
            # If it equals nums[index - 2], skip (don't copy)
        
        return index


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,1,1,2,2,3]
    nums1 = [1,1,1,2,2,3]
    print("Input:", nums1)
    k = sol.removeDuplicates(nums1)
    print("Output:", k, "nums =", nums1[:k], nums1[k:])
    print()
    
    # Test case 2: [0,0,1,1,1,1,2,3,3]
    nums2 = [0,0,1,1,1,1,2,3,3]
    print("Input:", nums2)
    k = sol.removeDuplicates(nums2)
    print("Output:", k, "nums =", nums2[:k], nums2[k:])
    print()
    
    # Test case 3: [1,1,1,1]
    nums3 = [1,1,1,1]
    print("Input:", nums3)
    k = sol.removeDuplicates(nums3)
    print("Output:", k, "nums =", nums3[:k], nums3[k:])
    print()
    
    # Test case 4: [1,2,3,4]
    nums4 = [1,2,3,4]
    print("Input:", nums4)
    k = sol.removeDuplicates(nums4)
    print("Output:", k, "nums =", nums4[:k], nums4[k:])