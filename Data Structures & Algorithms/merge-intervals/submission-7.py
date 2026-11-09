class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # need to sort it in ascending order using lambda function
        intervals.sort(key = lambda x: x[0])
        final = []
        
        # intervals=[[1,2],[3,4]]
        #                    i 

        prev_start = intervals[0][0] # just to init it with some values
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)): # start after the first one since we alr have it
            # Case 1: the previous end is less, so we can append that one rn
            if intervals[i][0] > prev_end:
                final.append([prev_start, prev_end])
                prev_start, prev_end = intervals[i][0], intervals[i][1]
            else:
                # must take a new start and new end
                prev_start = min(intervals[i][0], prev_start)
                prev_end = max(intervals[i][1], prev_end)
            
        final.append([prev_start, prev_end])
        return final



        


