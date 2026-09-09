class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isPalindrome(l, r):
            while l < r:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            return True
        
        while l < r:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return (isPalindrome(l, r-1) or isPalindrome(l+1, r))
        return True