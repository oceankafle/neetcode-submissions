class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for string in strs:
            # for each string, we want to count freq of char and store in arr
            alpha = [0] * 26

            for char in string:
                alpha[ord(char)-ord('a')] += 1
            
            mapping[tuple(alpha)].append(string)
            
        return list(mapping.values())