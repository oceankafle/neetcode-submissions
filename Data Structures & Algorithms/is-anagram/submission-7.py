class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_set = {}
        t_set = {}

        for i in range(len(s)):
            s_set[s[i]] = s_set.get(s[i], 0) + 1 # creates the dict for s string
            t_set[t[i]] = t_set.get(t[i], 0) + 1 # creates the dict for t string
        
        for char in s_set:
            if s_set[char] != t_set.get(char, 0):
                return False
        return True




