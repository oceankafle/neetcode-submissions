class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # two pointers, left and right pointer 
        # word1="abcd", word2="pq"
        res = ""

        r = min(len(word1), len(word2))
        l = 0 

        while l < r: # only iterates through the shortest string
            res += word1[l]
            res += word2[l]
            l += 1
        

        res += word1[l:]
        res += word2[l:]
        
        return res
