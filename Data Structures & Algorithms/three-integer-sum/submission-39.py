class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # to do 3sum, we have to first find a non-duplicate, then treat that as the first and do 2sum
        #

        # nums = [-4, -1, -1, 0, 1, 2]

        nums.sort()
        r = len(nums) - 1
        triplets = [] # append all valid triplets to this
        print(nums)

        # section to find the first number for the 3sum
        for i in range(len(nums)):
            # edge case where there's no possible numbers to equal up to 0
            if nums[i] > 0:
                break 
            elif i > 0:
                if nums[i - 1] == nums[i]: # if there's a duplicate, we need to skip this iteration
                    continue

            l = i + 1
            r = len(nums) - 1 # initialize it at the end
        
            while l < r:
                addedSum = nums[i] + nums[l] + nums[r]

                if addedSum == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]: # move the left pointer if there's duplicates
                        l += 1
                elif addedSum < 0:
                    l += 1
                else: # in the case where addedSum > 0, so we need to move right pointer down
                    r -= 1

        return triplets
        

            


