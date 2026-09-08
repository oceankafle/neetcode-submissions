class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 # keep track of the longest length seen so far
        numSet = set(nums)


        for num in nums: # 2
            if (num - 1) not in numSet:
                length = 1 # start it here

                while (num + length) in numSet: # 2 + 4
                    length += 1 # length = 4
                longest = max(longest, length)
        
        return longest
