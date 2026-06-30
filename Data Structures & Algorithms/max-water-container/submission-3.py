class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights = [1, 7, 2, 5, 4, 7, 3, 6]
        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l < r:
            width = (r - l)
            maxArea = max(maxArea, width * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea
            
        