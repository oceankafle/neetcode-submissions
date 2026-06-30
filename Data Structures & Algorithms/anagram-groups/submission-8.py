class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # --> {[1, 0, 1, .., ]: ["act"], }
        # for each anagram, map it to an alphabet 0's and 1's

        for string in strs: # "act"
            alpha = [0] * 26
            
            for char in string: # a
                alpha[ord(char)-ord('a')] += 1

            res[tuple(alpha)].append(string)            
        
        return list(res.values())
    
