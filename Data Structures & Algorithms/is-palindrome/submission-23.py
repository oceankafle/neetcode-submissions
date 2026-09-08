class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use .join to eliminate all the spaces in the string 
        new_string = s.replace(" ", "")

        # alternative: just skip if it encounters a space " "
        print(new_string)
        l, r = 0, len(new_string) - 1

        while l < r:
            # make sure to convert each one to either upper or lower case
            left_char = new_string[l].upper() 
            right_char = new_string[r].upper()
            print(left_char) # O
            print(right_char) # P
            
            if left_char == right_char:
                print("Hi!")
                l += 1
                r -= 1
            elif left_char.isalnum() == False:
                print("Hello!")
                l += 1
            elif right_char.isalnum() == False:
                print("Hi! The right window char is invalid here so decrementing r!")
                r -= 1
            elif left_char != right_char:
                print("Hey!")
                return False
            else:
                print("Yo!")
                return False
        print("You reached the end!")
        return True



            

