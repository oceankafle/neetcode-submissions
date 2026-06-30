class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freqSet = {}

        for i, val in enumerate(nums): # 1, 4
            difference = target - val  # difference = 7 - 4 = 3

            if difference in freqSet:   # if 3 in freqset (since 4 is the key)
                return [freqSet[difference], i]  # [0, 1] = freqset[difference], i
            freqSet[val] = i           # {3: 0}
        
