class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create two hashmaps for each string, keeps track of their char counts
        # first off, if the len of the strings isn't equal then immediately wrong
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False
        
        #then we can iterate using each s string or t, since they're equal in lengh
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for char in s:
            if countS.get(char) != countT.get(char):
                return False
        return True
        
        print(countS)
        print(countT)
        return True
