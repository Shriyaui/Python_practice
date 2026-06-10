class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(current, remaining):
            # Base case: if no remaining numbers, we have a complete permutation
            if not remaining:
                result.append(list(current))
                return
            
            # Try each number in the remaining list
            for i in range(len(remaining)):
                # Choose the current number
                current.append(remaining[i])
                # Remove it from remaining and recurse
                backtrack(current, remaining[:i] + remaining[i+1:])
                # Backtrack: remove the last added number
                current.pop()
        
        backtrack([], nums)
        return result


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,3]
    print("Test case 1:")
    print("Input: nums = [1,2,3]")
    print("Output:", sol.permute([1,2,3]))
    print()
    
    # Test case 2: [0,1]
    print("Test case 2:")
    print("Input: nums = [0,1]")
    print("Output:", sol.permute([0,1]))
    print()
    
    # Test case 3: [1]
    print("Test case 3:")
    print("Input: nums = [1]")
    print("Output:", sol.permute([1]))
    print()
    
    # Test case 4: [1,2,3,4] (partial output due to length)
    print("Test case 4:")
    print("Input: nums = [1,2,3,4]")
    result = sol.permute([1,2,3,4])
    print("Number of permutations:", len(result))
    print("First 5 permutations:", result[:5])