class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = {}

        for num in nums:
            mapping[num] = 1 + mapping.get(num, 0)
        
        for key, value in mapping.items():
            if value > 1:
                return True
        return False