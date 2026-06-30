class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or len(t) == 0:
            return ""
        
        countT = {} # need
        window = {} # keep track of char freq in a given window
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        have, need = 0, len(countT)
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0) # add extracted char to our window

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # shrink window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1 
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""