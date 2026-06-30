class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index] in monotonic decreasing order

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # [73] and we're at 74
                stackT, stackIdx = stack.pop() # pair
                res[stackIdx] = (i - stackIdx)
            stack.append([t, i])
        return res


    

