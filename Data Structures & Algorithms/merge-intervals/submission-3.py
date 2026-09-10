class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        
        merged = [intervals[0]] # [[1, 3]]

        for start, end in intervals[1:]: # [1, 5]
            if start > merged[-1][1]:
                merged.append([start, end])
            # overlapping
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], end)]
        
        return merged
