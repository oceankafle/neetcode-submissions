class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # countS, use the index as the key 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        print(countS)
        print(countT)
        for key, value in countS.items():  # prints the keys of the dict (j, a, r)
            if countS[key] != countT.get(key, 0):
                return False
        return True

        # loop through the entirety of a string
        # tally up the characters in both S string and T string

        # loop through the S hashset and compare it to the T hashset at each key.
        # if at any point they don't match up, return False
        




