class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # don't want duplicate triplets either
        # find the first elem to start on thats not a dupe
        # do 2 sum from there bc we already know our triplet value (or idx)
        nums.sort()
        print(nums) # [-4, -1, -1, 0, 1, 2]
                    #   0   1   2  3  4  5
        final = []

        for i in range(len(nums)): # i = 1
            if nums[i] > 0:
                break

            if i > 0 and nums[i-1] == nums[i]:
                continue

            # init the other pointers now since we have found a valid "state" , the num we're on
            l = i + 1

            r = len(nums) - 1

            while l < r:
                sumof3 = nums[i] + nums[l] + nums[r]
                if sumof3 > 0:
                    r -= 1
                elif sumof3 < 0:
                    l += 1
                else:
                    final.append([nums[i], nums[l], nums[r]])
                    l += 1 # move both pointers inwards
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: # skip duplicates at the left pointer
                        l += 1
        return final

