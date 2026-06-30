class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures = [30,38,30,36,35,40,28]

        res = [0] * len(temperatures)
        stack = [] # pair--> (temp, stackIdx) monotonic decreasing stack 

        for i, curr_temp in enumerate(temperatures):
            while stack and curr_temp > stack[-1][0]: # 38 > 30
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = (i - stackIdx)
                #stack.append([curr_temp, i])
            stack.append([curr_temp, i])
        
        return res


        


    

