class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window where we want to expand the window if it works
        # if condition is not valid, then we want to shrink the window and remove the l char

        l = 0
        seen = set() #
        # maintain a seen set to track what we've seen so far 
        longest = 0

        for r in range(len(s)): #r = 2 input = "abcabcbb"
            while s[r] in seen: # "c"
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r]) # {a, b, c}
            longest = max(longest, r - l + 1) # longest = 3
            #print("longest is this value right now!", longest)
            #print("This is what our seen set looks like right now", seen)
        
        return longest

