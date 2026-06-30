class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        # loop through each word in the strs, freq of char in a hashmap
        # while in that loop, check if that freq char exists in the final list?

        for string in strs: # "act"
            new = [0] * 26   # [0,0,0,0,0,0,0,0,0,0,0,0,0]
            for s in string: # "a"
                # build a arr --> [1,0,1, ....,1]
                new[ord(s) - ord('a')] += 1
            final[tuple(new)].append(string)
        return list(final.values())


