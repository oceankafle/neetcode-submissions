class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if there are overlapping intervals, take the min of one, and max of other
        res = [] # final output array 

        for i in range(len(intervals)):
            # easiest case, we append and then return the rest of the arrays
            if newInterval[1] < intervals[i][0]: # new end < interval start
                res.append(newInterval)
                return res + intervals[i:] # easy way to append the rest
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # don't append new one yet,could overlap later
            # we have an overlap and need to merge
            else:
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                newInterval = [start, end] # [1, 6]

        res.append(newInterval)    
        return res





