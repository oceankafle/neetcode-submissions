class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # heights = [2, 1, 5, 6, 2, 3]

        stack = [] # pair: (idx, height)
        maxArea = 0

        for i, curr_height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > curr_height:
                stackIdx, stackHeight = stack.pop()
                maxArea = max(maxArea,(i - stackIdx) * stackHeight)
                start = stackIdx
            stack.append((start, curr_height))

        # if there's leftover vals in stack that are the pairs that can be extended
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

         



