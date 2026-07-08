class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # substring = contiguous stays in order 
        # left and right pointer, either keep extending right or move left (and extend from that new point)

        charSet = set() # keep track of charFreq for the window we're on rn 
        # build up the window to find longest length
        l, r = 0, 1
        longest = 0

        if len(s) == 1:
            return 1
        
        if len(s) == 0:
            return 0
        charSet.add(s[l])


        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r]) # {b, }
                r += 1
            elif s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            longest = max(longest, (r - l + 1))

        return longest - 1
                


