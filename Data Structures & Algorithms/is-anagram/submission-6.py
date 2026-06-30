class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1 # creates the dict for s string
            countT[t[i]] = countT.get(t[i], 0) + 1 # creates the dict for t string
        
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        return True




