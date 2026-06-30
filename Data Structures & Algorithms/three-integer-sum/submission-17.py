class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        # nums = [-1, -1, 0, 1, 2, 3]
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # means we're at the index with a unique val and have skipped all duplicates
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
        
                if currSum == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                elif currSum < 0:
                    l += 1
                else:
                    r -=1 
        return triplets