class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # "pwwkew"


        seen = set() # seen = (p,w), len = 2
        length = 0
        l = 0
        
        for r in range(len(s)): # l = 0, r = 2
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = max(length, (r-l+1))
        return length


            








