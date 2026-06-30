class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {} # key:value --> value from nums: idx from nums

        for idx, val in enumerate(nums):
            difference = target - val

            if difference in mapping:
                return [mapping[difference], idx]
            
            mapping[val] = idx
        

