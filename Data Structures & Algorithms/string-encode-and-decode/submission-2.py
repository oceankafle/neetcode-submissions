class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s   # format: 4#neet
        return res




    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):  # each iteration of this loop reads one word
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j + 1 + length])
            i = j + 1 + length # beginning of next str, or end of entire str
        return res