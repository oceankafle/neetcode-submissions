class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1


        while l < r:
            while l < r and self.alphaNum(s[l]) == False: # means we hit a space or non alpha char
                l += 1
            while l < r and self.alphaNum(s[r]) == False:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))