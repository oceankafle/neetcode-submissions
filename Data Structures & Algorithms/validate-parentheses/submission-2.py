class Solution:
    def isValid(self, s: str) -> bool:
      # Runtime: O(n) because we are going through the input string once
      # Memory: O(n) because the stack could be as big as the size of string

      stack = []
      closeToOpen = {")" : "(", "]": "[", "}": "{"} 

      for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]: # stack isn't empty and the top of the stack is the same as the char we just checked
                stack.pop()                            # pop from the top
            else:
                return False 
        else:
            stack.append(c)
      return True if not stack else False    
