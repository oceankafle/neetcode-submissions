class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a sliding window?
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet: # indicates the start of a sequence
                length = 0
            
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest




            


