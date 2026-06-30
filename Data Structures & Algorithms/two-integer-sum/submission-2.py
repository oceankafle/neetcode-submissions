class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        # PrevMap = {}
        for idx, val in enumerate(nums):
            difference = target - val

            if difference in prevMap:
                return [prevMap[difference], idx]

            prevMap[val] = idx
        return []