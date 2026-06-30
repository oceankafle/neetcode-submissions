class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS_set = {}
        countT_set = {}

        for i in range(len(s)): # s and t are the same length
            countS_set[s[i]] = 1 + countS_set.get(s[i], 0)
            countT_set[t[i]] = 1 + countT_set.get(t[i], 0)

        for char in countS_set:
            if countS_set[char] != countT_set.get(char, 0):
                return False
        return True

        




