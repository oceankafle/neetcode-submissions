class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we also need to preserve contiguous though so we'll use a sliding window
        # for each interval, create a dictionary and map chars --> freq
        # if we take the len(slidingwindowString) - mostFreqChar, that will give us numReplacements
        # we will continuously calculate the longest possible seq at each sliding window and keep track of longest
        
        # {'A': 4, 'B': 3}
        freq = {}
        l = 0 
        longest = 0
        most_freq = 0

        
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            most_freq = max(freq.values())

            print("This is freq dict: ", freq)
            print("This is the count of the most freq char: ", most_freq)

            # Below tells you how many characters you'd need to change to make the entire window consist of only the most frequent character
            # This checks if the number of required changes exceeds k.

            while (r - l + 1) - most_freq > k: # means we need more replacements than given by k in order to make it all the same string
                # shrink the window
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, (r-l+1))
            print("This is the length of longest substring so far...", longest)
        return longest






            
        