class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        # len of nums = 7
        charFreq = {}
        maxCount = 0
        res = 0

        majority = (n // 2) + 1
        print(majority)
        
        for num in nums:
            charFreq[num] = 1 + charFreq.get(num, 0)
            res = num if charFreq[num] > maxCount else res
            maxCount = max(maxCount, charFreq[num])

        return res


