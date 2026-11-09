class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trackingDict = {}
        # idea of what I want to do:
        # keep a dictionary which maps te val in the nums arr to its index
        # then i will iterate through the 

        for idx, val in enumerate(nums): # 1, 4
            print(idx)
            print(val)
            difference = target - val # 7 - 4 = 3. is 3 in our dictionary? yes. add it
            # 

            if difference in trackingDict:
                # perform some logic 
                return [trackingDict[difference], idx]
            else:
                trackingDict[val] = idx # {3: 0, }
        
        return
        
 