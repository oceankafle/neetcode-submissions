class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return 
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)  # didn't add anything to it
        
        dfs(0, [], 0)
        return res

# Runtime: O(2 ^ t) where t is the target value
# Space: O(t/m) where t is target and m is min val in arr 