class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # Sort the array to easily skip duplicates
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack(current):
            # Base case: if current permutation is complete
            if len(current) == len(nums):
                result.append(list(current))
                return
            
            for i in range(len(nums)):
                # Skip if the number is already used
                if used[i]:
                    continue
                
                # Skip duplicates: if the current number is same as previous
                # and the previous number hasn't been used in this position yet
                # This ensures we only use the first occurrence of duplicate numbers
                # at each position
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # Choose the number
                used[i] = True
                current.append(nums[i])
                # Recurse
                backtrack(current)
                # Backtrack
                current.pop()
                used[i] = False
        
        backtrack([])
        return result


# Alternative approach using frequency counter (more efficient for many duplicates)
class Solution2(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # Count frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        def backtrack(current):
            # Base case: if current permutation is complete
            if len(current) == len(nums):
                result.append(list(current))
                return
            
            # Try each unique number
            for num in list(freq.keys()):
                if freq[num] > 0:
                    # Choose this number
                    current.append(num)
                    freq[num] -= 1
                    # Recurse
                    backtrack(current)
                    # Backtrack
                    current.pop()
                    freq[num] += 1
        
        backtrack([])
        return result


# Alternative approach using swapping (with duplicate handling)
class Solution3(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        
        def backtrack(start):
            # Base case: if we've processed all positions
            if start == len(nums):
                result.append(list(nums))
                return
            
            seen = set()
            for i in range(start, len(nums)):
                # Skip if we've already used this value at this position
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                
                # Swap the current index with the start index
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse to fix the next position
                backtrack(start + 1)
                # Swap back to restore the original array
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return result


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,1,2]
    print("Test case 1:")
    print("Input: nums = [1,1,2]")
    print("Output:", sol.permuteUnique([1,1,2]))
    print()
    
    # Test case 2: [1,2,3]
    print("Test case 2:")
    print("Input: nums = [1,2,3]")
    print("Output:", sol.permuteUnique([1,2,3]))
    print()
    
    # Test case 3: [2,2,1,1]
    print("Test case 3:")
    print("Input: nums = [2,2,1,1]")
    result = sol.permuteUnique([2,2,1,1])
    print("Number of permutations:", len(result))
    print("First 5 permutations:", result[:5])
    print()
    
    # Test case 4: [1]
    print("Test case 4:")
    print("Input: nums = [1]")
    print("Output:", sol.permuteUnique([1]))