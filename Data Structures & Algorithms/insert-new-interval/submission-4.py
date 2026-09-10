class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # can add everything after it
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # can add the current one immediately
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                newInterval = [start, end] # [1, 6]
        
        res.append(newInterval)
        return res
            