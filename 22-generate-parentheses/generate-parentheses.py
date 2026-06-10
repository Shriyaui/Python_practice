class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current, open_count, close_count):
            # Base case: valid combination complete
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add '(' if we haven't used all n open parentheses
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # Add ')' if we have more open than close parentheses
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: n = 3
    print("n = 3:", sol.generateParenthesis(3))
    
    # Test case 2: n = 1
    print("n = 1:", sol.generateParenthesis(1))
    
    # Test case 3: n = 2
    print("n = 2:", sol.generateParenthesis(2))