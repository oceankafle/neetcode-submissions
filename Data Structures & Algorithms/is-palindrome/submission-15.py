class Solution:
    def isPalindrome(self, s: str) -> bool:
        # put a left pointer at beginning, right pointer at end
        # if left ever crosses right, then stop bc we've went through the whole string
        
        # use isUpper() for O(1) time

        l = 0
        r = len(s) - 1

        while l < r: # meaning they are in a valid state to be compared
            # s= "race a car"
            #.     l.     r

            if self.alphaNum(s[l]) == True and self.alphaNum(s[r]) == True: # both valid
                if s[l].upper() == s[r].upper(): # valid state
                    l += 1
                    r -= 1
                else:
                    return False # invalid state
            
            elif self.alphaNum(s[l]) == False and self.alphaNum(s[r]) == True:
                l += 1
                continue

            elif self.alphaNum(s[l]) == True and self.alphaNum(s[r]) == False:
                r -= 1
                continue
            else: # both non-alphanumeric
                l += 1
                r -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
