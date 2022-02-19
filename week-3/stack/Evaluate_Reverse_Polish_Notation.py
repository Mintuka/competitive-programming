class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == operators[0]:
                    calc = stack.pop(-2) + stack.pop(-1)
                elif tokens[i] == operators[1]:
                    calc = stack.pop(-2) - stack.pop(-1)
                elif tokens[i] == operators[2]:
                    calc = stack.pop(-2) * stack.pop(-1)
                else:
                    calc = int(stack.pop(-2) / stack.pop(-1))

                stack.append(calc)
                
            i += 1
            
        return stack[0]