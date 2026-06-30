class Solution:

    def encode(self, strs: List[str]) -> str:
        # ['Hello', 'World']
        encoded = ""
        for thing in strs:
            print(thing)
            newWord = str(len(thing)) + "#" + thing
            encoded += newWord

        return encoded



    def decode(self, s: str) -> List[str]:
        final = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            # means we can start with extracting the word now + add it to final arr
            lenOfWord = int(s[i:j])
            extractedWord = s[j+1:j+1+lenOfWord]
            print(extractedWord)
            i = j + 1 + lenOfWord
            final.append(extractedWord)
        
        print(final)
        return final
            
            #   5#World5#Ocean




