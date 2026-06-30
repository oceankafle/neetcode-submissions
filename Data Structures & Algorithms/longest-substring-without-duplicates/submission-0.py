class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charMap = set() # holds unique values only

        for r in range(len(s)):
            while s[r] in charMap:
                charMap.remove(s[l])
                l += 1
            charMap.add(s[r])
            res = max(res, r - l + 1)
        return res

