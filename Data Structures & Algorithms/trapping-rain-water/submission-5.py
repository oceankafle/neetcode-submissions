class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1 # start left at beginning, right at end
        leftMax, rightMax = height[l], height[r] # initialize these as their beginning values 
        res = 0

        while l < r:
            if leftMax <= rightMax:
                l += 1
                res += max(0, leftMax - height[l]) # don't have to check for negative because of line above
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res