class Solution:

    def encode(self, strs: List[str]) -> str: # ["Hello", "World", "Ocean"]
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string  # res = "5#Hello5#World5#Ocean"
        
        #print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            extracted_word = s[j + 1:j + 1 + length]
            res.append(extracted_word)
            i = j + 1 + length
        return res

