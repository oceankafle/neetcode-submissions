class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we use a dictionary
        countFreq = {}     # {3:0, 4: 1, 5: 2, }
        # calculate diff by val + 


        for idx, val in enumerate(nums): # 3, 6
            difference = target - val  # 7 - 6 = 1

            if difference in countFreq:
                return [countFreq[difference], idx]
            
            countFreq[val] = idx # 
        
        return 
