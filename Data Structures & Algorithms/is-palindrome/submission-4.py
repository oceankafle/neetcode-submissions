class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]): # check left char
                l += 1
            while l < r and not self.alphaNum(s[r]): # check right char
                r -= 1
            
            # so now both chars are valid
            if s[l].lower() == s[r].lower(): # if the chars are the same
                l += 1 
                r -= 1
            else:
                return False
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or # upper
                ord('a') <= ord(c) <= ord('z') or # lower
                ord('0') <= ord(c) <= ord('9')) # num


        
