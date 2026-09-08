class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use .join to eliminate all the spaces in the string 
        #new_string = s.replace(" ", "")
        l, r = 0, len(s) - 1

        while l < r:
            # make sure to convert each one to either upper or lower case
            left_char = s[l].upper() 
            right_char = s[r].upper()
            
            if left_char == right_char:
                l += 1
                r -= 1
            elif left_char.isalnum() == False:
                l += 1
            elif right_char.isalnum() == False:
                r -= 1
            elif left_char != right_char:
                return False
            else:
                return False
        return True
    
    # time complexity: 
    # space complexity: 



            

