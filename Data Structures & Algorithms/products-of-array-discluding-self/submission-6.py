class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 4, 6]
        #
        
        res = [1] * (len(nums)) # [48, 24, 12, 8]
        # pre fix pass then post fix pass
        prefix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        # post fix pass
        postfix = 1
        for i in range(len(nums)-1, -1, -1): # i = 0
            res[i] *= postfix              # res[0] *= 48
            postfix *= nums[i] # pf = 48
        
        return res



