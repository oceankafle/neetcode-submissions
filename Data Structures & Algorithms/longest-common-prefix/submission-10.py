class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])): #picking arbitrarily, handle out of bounds case
            for s in strs: # iterate through other words and check the chars in that position
                if i == len(s):
                    return res
                elif s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res