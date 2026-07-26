class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # stack = [4, 13, 5]
        total = 0

        for i in range(len(tokens)): # i = 
            if tokens[i] in "+-*/":
                a = int(stack.pop()) 
                b = int(stack.pop())
            
                if tokens[i] == "+":
                    stack.append(a + b) # stack = []

                if tokens[i] == "-":
                    stack.append(b-a)

                if tokens[i] == "*":
                    stack.append(a*b) # stack = []

                if tokens[i] == "/":
                    stack.append(int(b / a))
            else:
                stack.append(int(tokens[i])) # append the number onto the stack

        return int(stack[0])
            
