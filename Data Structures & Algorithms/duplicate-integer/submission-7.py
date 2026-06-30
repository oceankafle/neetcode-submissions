class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        charSet = set()

        for num in nums:
            if num in charSet:
                return True
            else:
                charSet.add(num)
        return False