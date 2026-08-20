class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # two pointers, left and right pointer 
        # word1="abcd", word2="pq"
        res = ""

        if len(word1) > len(word2):
            r = len(word2)
        else:
            r = len(word1)

        l = 0 

        while l < r: # only iterates through the shortest string
            res += word1[l]
            res += word2[l]
            l += 1
        
        if len(word1) > len(word2):
            res += word1[l:]
        else:
            res += word2[l:]
        
        return res
