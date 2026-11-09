class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we want to count the number of each char first in dict for each string
        # map that to a list with 26 zeroes, which index mapped to char in alphabet
        # the list is the key though, and the value will be anohter [] where we append if
        # they match.

        charDict = {}
        other = defaultdict(list)

        for string in strs:
            alpha = [0] * 26
            for char in string:
                charDict[char] = 1 + charDict.get(char, 0)
                alpha[ord(char) - ord('a')] += 1
            
            other[tuple(alpha)].append(string)


        res = list(other.values())
        return res
