class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        
        charSet = set() # set = {z, } 
        l = 0
        r = 0
        longest = 0

        while r < len(s):
            if s[r] in charSet:
                charSet.remove(s[l])
                l += 1 
            else:
                charSet.add(s[r])
                r += 1
            longest = max(longest, (r - l))
        return longest