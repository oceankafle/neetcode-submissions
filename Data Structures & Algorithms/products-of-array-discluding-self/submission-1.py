class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre fix pass then post fix pass
        prefix = 1
        res = [1] * len(nums)
        # [1, 2, 4, 6]
        
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            # [1, 1, 2, 8]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res


