class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        # Edge Cases
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            for string in strs: # want to be able to compare it to every other string in the list
                if i == len(string) or string[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
