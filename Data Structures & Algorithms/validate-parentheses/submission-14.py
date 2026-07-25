class Solution:
    def isValid(self, s: str) -> bool:
        # s="([{}])"
       charDict = {"}": "{", ")": "(", "]": "["}
       stack = []

       for char in s:
        if char in charDict:
            if stack and stack[-1] == charDict[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char) # stack = [      ]
        
       if len(stack) == 0:
        return True
       else:
        return False
