class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # add frequency of the characters everytime it occurs 
            countT[t[i]] = 1 + countT.get(t[i], 0) # do the same frequency count for the t word as well 
        for char in countS:
            if countS[char] != countT.get(char, 0): # the number of times this character appears in string s vs countT dictionary
                return False
        return True



