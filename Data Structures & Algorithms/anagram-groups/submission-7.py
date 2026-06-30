
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        freq = {}


        # for each string --> create a array of 26 spots [1, 0, 0,..1]

        for string in strs: # "act"
            alpha = [0] * 26

            for char in string:
                alpha[ord(char) - ord('a')] += 1
            
            res[tuple(alpha)].append(string)
        return list(res.values())



