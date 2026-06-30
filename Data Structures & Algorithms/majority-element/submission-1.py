class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for thing in freq:
            if freq[thing] > (n // 2):
                return thing



