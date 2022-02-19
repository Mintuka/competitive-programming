class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                list = []
                
                while stack[-1] != '(':
                    list.append(stack.pop())
                stack.pop()
                
                while len(list):
                    stack.append(list.pop(0))
                    
            else:
                stack.append(s[i])
                
        return "".join(stack)