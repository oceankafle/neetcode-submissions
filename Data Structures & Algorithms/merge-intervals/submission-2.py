class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = [[1,3],[1,5],[6,7]]

        intervals.sort(key = lambda interval: interval[0]) # sort by start value
        print(intervals)

        merged = [intervals[0]] # add the first one since there's nothing to compare it with

        for start, end in intervals[1:]:
            previousEnd = merged[-1][1] # this gives us the prev end value

            if start > previousEnd: # we're in a valid state and can safely add
                merged.append([start, end])
            # overlap case, we need to modify what's in the merged arr
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], end)]
        
        return merged

        

