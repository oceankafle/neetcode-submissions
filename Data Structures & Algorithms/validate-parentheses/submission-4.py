class Solution:
    def isValid(self, s: str) -> bool:
        # Ex) "[(])"
        stack = []
        parentheses = {")":"(", "}": "{", "]": "["}

        for char in s: # "]"
            if char in parentheses:
                if stack and parentheses[char] == stack[-1]: # if char is a key in pDict
                    stack.pop()
                else:
                    return False    
            else:
                stack.append(char) # stack = [ "[", "(", ]
        
        return True if len(stack) == 0 else False


                
