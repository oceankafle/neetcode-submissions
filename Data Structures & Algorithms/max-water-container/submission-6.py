class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find width by subtracking the indices and using l and r pointer
        greatest_area = 0
        l, r = 0, len(heights) - 1


        while l < r:
            curr_area = (r-l) * min(heights[l], heights[r]) # (1) * 1
            greatest_area = max(curr_area, greatest_area) # GA = 1
            
            if heights[l] <= heights[r]: #l = 0, r = 1
                l += 1
            else:
                r -= 1

        
        return greatest_area

