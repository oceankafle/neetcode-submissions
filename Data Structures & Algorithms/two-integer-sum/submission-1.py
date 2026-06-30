class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = [] # create an output array
        prevMap = {}  # value : index
        
        for index, number in enumerate(nums):
            difference = target - number
            
            if difference in prevMap:
                return [prevMap[difference], index]
            prevMap[number] = index

        return

