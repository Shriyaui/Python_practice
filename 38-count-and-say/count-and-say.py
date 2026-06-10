class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Base case
        if n == 1:
            return "1"
        
        # Start with the first term
        result = "1"
        
        # Generate terms from 2 to n
        for _ in range(2, n + 1):
            result = self.rle_encode(result)
        
        return result
    
    def rle_encode(self, s):
        """
        Perform run-length encoding on string s
        """
        if not s:
            return ""
        
        encoded = []
        count = 1
        
        # Iterate through the string
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # Same character, increment count
                count += 1
            else:
                # Different character, append count and character
                encoded.append(str(count))
                encoded.append(s[i - 1])
                count = 1
        
        # Append the last group
        encoded.append(str(count))
        encoded.append(s[-1])
        
        return ''.join(encoded)


# Alternative iterative approach without helper function
class Solution2(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        result = "1"
        
        for _ in range(2, n + 1):
            current = ""
            count = 1
            
            # Encode the current result
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    current += str(count) + result[i - 1]
                    count = 1
            
            # Add the last group
            current += str(count) + result[-1]
            result = current
        
        return result


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    print("n = 1:", sol.countAndSay(1))  # Output: "1"
    print("n = 2:", sol.countAndSay(2))  # Output: "11"
    print("n = 3:", sol.countAndSay(3))  # Output: "21"
    print("n = 4:", sol.countAndSay(4))  # Output: "1211"
    print("n = 5:", sol.countAndSay(5))  # Output: "111221"
    print("n = 6:", sol.countAndSay(6))  # Output: "312211"
    print("n = 7:", sol.countAndSay(7))  # Output: "13112221"
    print("n = 8:", sol.countAndSay(8))  # Output: "1113213211"
    print("n = 9:", sol.countAndSay(9))  # Output: "31131211131221"
    print("n = 10:", sol.countAndSay(10)) # Output: "13211311123113112211"