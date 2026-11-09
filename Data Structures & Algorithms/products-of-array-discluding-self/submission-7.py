class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum array
        # postfix sum array 
        prefix = 1
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)): # 3
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1): # 0
            res[i] *= postfix
            postfix *= nums[i]
    
        return res

            
            



