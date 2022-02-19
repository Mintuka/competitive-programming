class Solution:
    def isValid(self, s: str) -> bool:
        mapChar = {"(":")","[":"]","{":"}",")":False,"}":False,"]":False}
        i = 1
        stack = [s[0]]
        while i < len(s) and len(stack):
            if not mapChar[stack[-1]]:
                return False
            if mapChar[stack[-1]] != s[i]:
                stack.append(s[i])
            else:
                stack.pop()
                if not len(stack) and i != len(s) - 1:
                    stack.append(s[i+1])
                    i += 1
            
            i += 1
            
        
        
        return False if len(stack) else True