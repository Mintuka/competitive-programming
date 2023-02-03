class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split('/')
        result = deque()
        up = 0
        
        for i in range(len(stack)-1,-1,-1):
            if stack[i]:
                if stack[i] == '..':
                    up += 1
                elif stack[i] != '.' and stack[i] != '..':
                    if up:
                        up -= 1
                    else:
                        result.appendleft('/'+stack[i])
        
        return ''.join(result) if result else '/'