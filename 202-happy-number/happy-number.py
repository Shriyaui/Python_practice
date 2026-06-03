class Solution(object):
    def isHappy(self, n):

        visited = set()

        while n != 1:

            # If number is already seen, we're in a cycle
            if n in visited:
                return False

            visited.add(n)

            sum_of_squares = 0

            # Find sum of squares of digits
            while n > 0:
                digit = n % 10
                sum_of_squares += digit * digit
                n = n // 10

            n = sum_of_squares

        return True