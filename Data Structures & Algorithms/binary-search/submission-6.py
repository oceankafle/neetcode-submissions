class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1 # target = 4

        while l <= r: # l = 3, r = 5
            mid = (l + r) // 2 # mid = 4
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else: # nums[mid] > target
                r = mid - 1

        return -1