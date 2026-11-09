class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        final = []
        start = newInterval[0]
        end = newInterval[1]

        for i in range(len(intervals)): # 1
            # check if the newInterval is completely before it
            if intervals[i][1] < start:
                final.append(intervals[i])

            # check if the newInterval is completely after
            elif intervals[i][0] > end:
                final.append([start, end])
                return final + intervals[i:]

            else:# if the newInterval is somewhere in the middle
                start = min(intervals[i][0], start) # [1]
                end = max(intervals[i][1], end) # [5]
                
        final.append([start, end])
        
        return final

