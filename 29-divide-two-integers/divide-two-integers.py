class Solution(object):
    def divide(self, dividend, divisor):

        if dividend == -2147483648 and divisor == -1:
            return 2147483647  # 2^31 - 1
        
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive numbers
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        
        quotient = 0
        
        # Use bit manipulation to speed up subtraction
        # We'll subtract multiples of the divisor (doubling each time)
        while dividend_abs >= divisor_abs:
            temp = divisor_abs
            multiple = 1
            
            # Double the divisor until it's too big
            while dividend_abs >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            # Subtract the largest multiple found
            dividend_abs -= temp
            quotient += multiple
        
        # Apply the sign
        if negative:
            quotient = -quotient
        
        # Check for overflow (though we handled the main case already)
        if quotient > 2147483647:
            return 2147483647
        if quotient < -2147483648:
            return -2147483648
        
        return quotient


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: 10 / 3 = 3
    print("10 / 3 =", sol.divide(10, 3))
    
    # Test case 2: 7 / -3 = -2
    print("7 / -3 =", sol.divide(7, -3))
    
    # Test case 3: -10 / 3 = -3
    print("-10 / 3 =", sol.divide(-10, 3))
    
    # Test case 4: -7 / -3 = 2
    print("-7 / -3 =", sol.divide(-7, -3))
    
    # Test case 5: 0 / 5 = 0
    print("0 / 5 =", sol.divide(0, 5))
    
    # Test case 6: Overflow case
    print("-2147483648 / -1 =", sol.divide(-2147483648, -1))
    
    # Test case 7: Large numbers
    print("2147483647 / 1 =", sol.divide(2147483647, 1))