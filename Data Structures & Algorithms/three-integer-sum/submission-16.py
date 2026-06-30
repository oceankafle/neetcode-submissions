class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]: # its a duplicate
                continue
            
            l = i + 1
            r = len(nums) - 1
            # means we're not at a duplicate so we need to check now
            while l < r:
                currSum = val + nums[l] + nums[r]
                if currSum == 0:
                    triplets.append([val, nums[l], nums[r]])
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
                


























# question: could you not just create a set from nums and then sort that?