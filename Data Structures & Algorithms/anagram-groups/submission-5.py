
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a res arr
        # create a dict with defaultdict(list) -> each key maps to a list
        res = defaultdict(list)

        for string in strs:    # act, pots, tops, cat, 
            count = 26 * [0]   # to count each one

            for char in string:
                count[ord(char) - ord('a')] += 1

            res[tuple(count)].append(string)
        
        return list(res.values())

