
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # creates dict with empty lists as key

        for string in strs:
            count = [0] * 26  # create arr to keep track of char count

            for char in string: # "act"
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(string)
        
        return list(result.values())