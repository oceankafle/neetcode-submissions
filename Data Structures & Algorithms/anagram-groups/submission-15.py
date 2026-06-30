class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # General Idea
        
        # for each word in strs --> construct arr[] that uses 0s and 1s to track it alphabetically
        # use that array as a key in our dict, append words as values if they have same key
        # return an array of all the items from our dictionary
        mapping = defaultdict(list)
        final = []

        for word in strs:
            alpha = [0] * 26 # want to fill this out for each word 
            # ex) act = [1,0,1,0,0,....1..0]
            for char in word:
                alpha[ord(char) - ord('a')] += 1
            #print(alpha)
            mapping[tuple(alpha)].append(word)
        #print(mapping) 
        final.append(mapping.values())
        new = list(mapping.values())
        print(new)
        return new

