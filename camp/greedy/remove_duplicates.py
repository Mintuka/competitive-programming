class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        duplicates = Counter(s)
        visited = set()
        
        for char in s:
            
            while stack and char not in visited and char < stack[-1] and duplicates[stack[-1]]:
                visited.discard(stack.pop())
                
            char not in visited and stack.append(char)
            
            visited.add(char)
            duplicates[char] -= 1
            
        return "".join(stack)