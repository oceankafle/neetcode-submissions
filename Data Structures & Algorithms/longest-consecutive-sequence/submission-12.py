class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tracking = set(nums)
        longest = 0

        for num in tracking:
            length = 1
            if (num - 1) not in tracking:
                length = 1
            
                while (num + length) in tracking:
                    #longest += 1
                    length += 1
                longest = max(longest, length)
        
        return longest
    
        # set = {2, 3, 4, 5, 10, 20}
        #        .
        #
        # longest = 3
        # length = 4