class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Calculate width between the two lines
            width = right - left

            # Height of water is limited by the shorter line
            h = min(height[left], height[right])

            # Current area
            area = width * h

            # Update maximum area found so far
            max_water = max(max_water, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water