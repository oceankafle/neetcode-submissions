class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # freqDict = {A: 4, B: 3}
        freqDict = {}
        maxFreq = 0
        l = 0
        longest = 0

        # count the freq of each char, take the smaller one - k, then add that to the most freq Char
        
        for r in range(len(s)):
            freqDict[s[r]] = 1 + freqDict.get(s[r], 0)

            maxFreq = max(freqDict[s[r]], maxFreq) # longest we've seen so far
            print(freqDict)

            while (r - l + 1) - maxFreq > k: # window - maxF = num of replacements we need is not val
                freqDict[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest




        # find max --> 4
        # at each window, check length of our current longest string that has all same chars by using maxF



            



















