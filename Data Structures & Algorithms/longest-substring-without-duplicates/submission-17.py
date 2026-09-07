class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window for contiguous
        charSet = set()
        maxWindow = 0

        if len(s) == 0:
            return 0 
        if len(s) == 1:
            return 1
        
        l = 0 # l = 0, r = 2

        for r in range(len(s)): # "pwwkew", s[2] = w, charSet = (p, w)
            while s[r] in charSet:
                # we want to remove the left character to shrink the window, then increment left pointer
                charSet.remove(s[l])
                l += 1
            # handle chars that are valid and can be added to the window
            charSet.add(s[r])
            maxWindow = max(maxWindow, (r - l) + 1) # maxWindow = 2
            #r += 1
        
        return maxWindow

        
        
