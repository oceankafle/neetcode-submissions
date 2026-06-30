class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}
        res, resLen = [-1, -1], float("infinity")

        # {'X': 1, 'Y': 1, 'Z': 1}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        have, need = 0, len(countT)
        
        l = 0
        for r in range(len(s)):
            char = s[r] # extract the char on right side of sliding window

            # add the char to the window
            window[char] = 1 + window.get(char, 0)

            # check if the char we just added was "important"
            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                # check if we are at the smallest window length so far
                if (r - l + 1) < resLen:
                    res = [l, r] # track down the indices it occurred at
                    resLen = (r - l + 1) # store the new length
                
                # We're not at the smallest window so remove the left side char from the window 
                window[s[l]] -= 1 
                if s[l] in countT and window[s[l]] < countT[s[l]]: # Check if we removed an "important" char
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""











        
