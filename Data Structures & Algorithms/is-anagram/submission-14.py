class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge cases
        if not s or not t:
            return False
        
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            # populate both of our dictionaries with char counts
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for key, value in countS.items():
            if value != countT.get(key, 0):
                return False
        return True



