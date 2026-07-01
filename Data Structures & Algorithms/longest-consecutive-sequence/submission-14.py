class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tracking = set(nums)
        # {2, 20, 4, 10, 3, 4, 5}
        

        # global length variable
        longest = 0

        for num in nums:
            if (num-1) not in tracking:
                # local variable to keep track of longest length seen SO FAR 
                length = 0
            
                # means we found a valid starting point
                while num + length in tracking:
                    length += 1
                
                longest = max(length, longest)
        
        return longest
            
