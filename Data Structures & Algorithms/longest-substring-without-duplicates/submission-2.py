class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        charSet = set()
        l = 0
        r = 0
        # calculation: (r - l + 1)
        # charSet = {x,y, }

        #   l r
        # "zxyzxyz"

        # l = 0, r = 1
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            length = max(length, r - l + 1) # len = 3 
            charSet.add(s[r])
            r += 1
        return length




