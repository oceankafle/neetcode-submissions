class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}
        l = 0

        # Creates the countT dictionary (need)
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")

        for r in range(len(s)):
            char = s[r] # extract the char at right pos
            window[char] = 1 + window.get(char, 0) # add it to the window dict

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen: # we found a smaller window so we need to update
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1 # pop the left
                if s[l] in countT and countT[s[l]] > window[s[l]]: # if char we just popped affects the "have" dict
                    have -= 1
                l += 1
                    
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""






