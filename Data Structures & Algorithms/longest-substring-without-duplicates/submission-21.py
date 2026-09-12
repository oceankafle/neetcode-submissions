class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set to hold unique chars, sliding window to take max window as we traverse


        charSet = set()
        l = 0
        longest = 0 # longest window length we've seen so far

        # s="zxyzxyz"

        for r in range(len(s)):
            while s[r] in charSet:
                # we want to remove the left char to decrease the window 
                charSet.remove(s[l])
                l += 1
            
            # we have a char we haven't seen before in the window, no duplicates
            charSet.add(s[r]) # charSet = ()
            longest = max(r - l + 1, longest) # compare it with the window we're on rn
        
        return longest
