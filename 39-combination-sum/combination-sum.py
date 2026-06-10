class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(remaining, start, current_combination):
            # Base case: found a valid combination
            if remaining == 0:
                result.append(list(current_combination))
                return
            
            # Base case: exceeded the target
            if remaining < 0:
                return
            
            # Try all candidates starting from 'start' to avoid duplicates
            # (using 'start' ensures we don't consider previous candidates again,
            # which would create permutations of the same combination)
            for i in range(start, len(candidates)):
                # Add the current candidate
                current_combination.append(candidates[i])
                # Recurse with reduced remaining target
                # Note: we pass i (not i+1) because we can reuse the same candidate
                backtrack(remaining - candidates[i], i, current_combination)
                # Backtrack: remove the last candidate
                current_combination.pop()
        
        # Sort candidates to potentially optimize (though not strictly necessary)
        candidates.sort()
        backtrack(target, 0, [])
        return result


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: candidates = [2,3,6,7], target = 7
    print("Test case 1:")
    print("Input: candidates = [2,3,6,7], target = 7")
    print("Output:", sol.combinationSum([2,3,6,7], 7))
    print()
    
    # Test case 2: candidates = [2,3,5], target = 8
    print("Test case 2:")
    print("Input: candidates = [2,3,5], target = 8")
    print("Output:", sol.combinationSum([2,3,5], 8))
    print()
    
    # Test case 3: candidates = [2], target = 1
    print("Test case 3:")
    print("Input: candidates = [2], target = 1")
    print("Output:", sol.combinationSum([2], 1))
    print()
    
    # Additional test case
    print("Test case 4: candidates = [2,3,6,7], target = 14")
    print("Output:", sol.combinationSum([2,3,6,7], 14))