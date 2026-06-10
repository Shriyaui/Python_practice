class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Handle edge case: if either number is "0", product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # Create an array to store the product digits
        # The product of two numbers with m and n digits has at most m + n digits
        result = [0] * (m + n)
        
        # Perform multiplication digit by digit from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Get the integer values of the digits
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # Calculate the product and add to the appropriate position
                # The product of digits at positions i and j goes to positions (i+j) and (i+j+1)
                pos1 = i + j
                pos2 = i + j + 1
                
                # Calculate the total sum at pos2 including the current product
                total = digit1 * digit2 + result[pos2]
                
                # Update the result array with the new digit and carry
                result[pos2] = total % 10
                result[pos1] += total // 10
        
        # Convert the result array to a string, skipping leading zeros
        # Find the first non-zero digit
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        
        # Build the result string
        result_str = ''.join(str(digit) for digit in result[start:])
        
        return result_str if result_str else "0"


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: "2" * "3" = "6"
    print(sol.multiply("2", "3"))
    
    # Test case 2: "123" * "456" = "56088"
    print(sol.multiply("123", "456"))
    
    # Test case 3: "0" * "123" = "0"
    print(sol.multiply("0", "123"))
    
    # Test case 4: "999" * "999" = "998001"
    print(sol.multiply("999", "999"))
    
    # Test case 5: Large numbers
    print(sol.multiply("123456789", "987654321"))