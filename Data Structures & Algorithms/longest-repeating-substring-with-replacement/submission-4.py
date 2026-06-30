class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        # "AAABABB" --> len(s) = 7
        # most freq char = "A" = 4 times
        # k is number of replacements allowed = 2

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0) # makes the freqDict

            while (r - l + 1) - max(freq.values()) > k: # size of window - mostFreqCharacter
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

