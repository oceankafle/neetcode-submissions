class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack (last in, first out)        
        # create a dictionary that can map the closing to the opening characters
        # ex) s="([{}])"
        charDict = {")": "(", "}":"{", "]":"["}
        stack = [] # this will hold the chars, push and pop from it

        for char in s: # }
            if char in charDict: # }
                print("I am in the charDict: ", char)
                if stack and stack[-1] == charDict[char]: # { 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char) # stack = [ ( [ {  ]

        if len(stack) == 0:
            return True
        return False

        
            