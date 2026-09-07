class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        numSet = set(nums)

        for num in numSet:   # start with 2
            if (num - 1) not in numSet:
                # start a sequence here 
                count = 1

                while (num + count) in numSet:     # 6
                    count += 1
            
                maxCount = max(maxCount, count)
        
        return maxCount


