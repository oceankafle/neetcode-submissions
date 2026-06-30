class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "Worlds"]
        # ["5#Hello6#World"] --> get it to this state by the end of this code
        encoded = ""
        for word in strs:
            encodedWord = str(len(word)) + "#" + word
            encoded = encoded + encodedWord
        print(encoded)
        return encoded
    
        # "5#Hello5#World"


    def decode(self, s: str) -> List[str]:
        final = []
        i = 0 # pointer 

        while i < len(s): # i = 0, j = 0
            j = i 

            while s[j] != "#": # i marks the beginning of the word
                j += 1 # goes up till the # 5#hello5#world
            
            
            lenofWord = int(s[i:j]) # 5
            print(lenofWord)

            convert = int(lenofWord)
            final.append(s[j+1:j+1+convert])
            #now jump to the next word
            i = convert + j + 1
        return final




