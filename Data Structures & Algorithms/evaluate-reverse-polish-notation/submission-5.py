class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "*", "-", "/"]
        # Ex) tokens = ["1","2","+","3","*"]
        # stack = [9] top 

        # traverse through input list, add the 2 and 1 to the stack.
        # once we hit a operand "+, *, -, /", we pop most recent 2 vals
        # val1 = 1, val2, 2 --> add val1 + val2 = 3. Push that to stack.
        # Next we hit 3 so we push that 3 onto the stack.
        # Next, we hit a operand "*", so we pop most recent 2 vals
        # val1 = 3, val2 = 3 --> val1 * val 2= 3 * 3 = 9. Push that onto stack.
        # we hit the end of the list so return stack[-1].

        for char in tokens:
            if char not in operands:
                stack.append(char) # stack = [9, 4]
            else: # means we hit an operand
                a = int(stack.pop()) # 3
                b = int(stack.pop()) # 3
                res = 0
                
                if char == "+":
                    res = a + b
                elif char == "*":
                    res = a * b
                elif char == "-":
                    res = b - a
                elif char == "/":
                    res = (int(float(b) / a))
                else:
                    raise ValueError("Invalid operator")
                stack.append(res)
        
        return int(stack[-1])
            
                
                










