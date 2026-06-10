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
        
        # Get lengths of both numbers
        len1, len2 = len(num1), len(num2)
        
        # Create an array to store intermediate results
        # Maximum length of product is len1 + len2
        result = [0] * (len1 + len2)
        
        # Perform multiplication digit by digit from right to left
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                # Multiply digits
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # Calculate product and add to the result array
                # Position in result array: i+j+1 for the units place
                product = digit1 * digit2
                
                # Add to the current position
                pos1 = i + j
                pos2 = i + j + 1
                
                total = product + result[pos2]
                
                # Store the result
                result[pos2] = total % 10
                result[pos1] += total // 10
        
        # Convert result array to string, skipping leading zeros
        result_str = ''.join(map(str, result))
        
        # Remove leading zeros
        result_str = result_str.lstrip('0')
        
        return result_str if result_str else "0"


# Alternative implementation with clear comments
class Solution2(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # Create a list to store the product digits
        # The product of two numbers with m and n digits has at most m + n digits
        product = [0] * (m + n)
        
        # Reverse the strings to make calculation easier from least significant digit
        num1_rev = num1[::-1]
        num2_rev = num2[::-1]
        
        # Multiply each digit of num1 with each digit of num2
        for i in range(m):
            for j in range(n):
                # Convert characters to integers
                digit1 = ord(num1_rev[i]) - ord('0')
                digit2 = ord(num2_rev[j]) - ord('0')
                
                # Multiply and add to the appropriate position
                product[i + j] += digit1 * digit2
                
                # Handle carry
                if product[i + j] >= 10:
                    product[i + j + 1] += product[i + j] // 10
                    product[i + j] = product[i + j] % 10
        
        # Reverse the product list to get the correct order
        product = product[::-1]
        
        # Convert to string, skipping leading zeros
        result = ''.join(map(str, product)).lstrip('0')
        
        return result if result else "0"


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: "2" * "3" = "6"
    print("Test case 1:")
    print("Input: num1 = '2', num2 = '3'")
    print("Output:", sol.multiply("2", "3"))
    print()
    
    # Test case 2: "123" * "456" = "56088"
    print("Test case 2:")
    print("Input: num1 = '123', num2 = '456'")
    print("Output:", sol.multiply("123", "456"))
    print()
    
    # Test case 3: "0" * "123" = "0"
    print("Test case 3:")
    print("Input: num1 = '0', num2 = '123'")
    print("Output:", sol.multiply("0", "123"))
    print()
    
    # Test case 4: "999" * "999" = "998001"
    print("Test case 4:")
    print("Input: num1 = '999', num2 = '999'")
    print("Output:", sol.multiply("999", "999"))
    print()
    
    # Test case 5: Large numbers
    print("Test case 5:")
    print("Input: num1 = '123456789', num2 = '987654321'")
    print("Output:", sol.multiply("123456789", "987654321"))