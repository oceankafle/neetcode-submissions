class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] # holds our final output

        # comparisons between the start times and end times, 
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # end of new less than start of curr
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else: # overlapping case
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                newInterval = [start, end] # [1, 6]
        
        res.append(newInterval)
        return res
            
        
