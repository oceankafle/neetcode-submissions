class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        # len of nums = 7
        charFreq = {}

        majority = (n // 2) + 1
        print(majority)
        
        for num in nums:
            charFreq[num] = 1 + charFreq.get(num, 0)
        
        for item in charFreq:
            if charFreq[item] >= majority:
                return item
        return 


