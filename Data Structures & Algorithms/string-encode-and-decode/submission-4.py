class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string)) + "#" + string
        return res
        # "4#neet4#code4#love3#you"

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i # j = 0
            while s[j] != "#": # j = 1
                j += 1
            # means we're at the pound char
            length = int(s[i:j]) # len = str[0:1]
            res.append(s[j + 1: j + 1 + length]) # entire str
            i = j + 1 + length
        
        return res




