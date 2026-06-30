class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {} # keep track of char frequencies
        res = [-1, -1] # hold the l,r pointers so we can slice the string at end
        resLen = float("infinity") # maintains the minimum length of a valid string throughout

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        l = 0
        have, need = 0, len(countT)

        for r in range(len(s)):
            char = s[r] # extract the actual char
            window[char] = 1 + window.get(char, 0)

            # Check if this char has fulfilled the requirements
            if char in countT and window[char] == countT[char]: # has to be exactly equal
                have += 1
            
            while have == need:
                # check if len of sliding window is the smallest so far
                if (r - l + 1) < resLen: # we have found a new min length to store
                    res = [l, r]
                    resLen = (r - l + 1)
                
                # Shrink our window by removing our left side
                window[s[l]] -= 1
                
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
