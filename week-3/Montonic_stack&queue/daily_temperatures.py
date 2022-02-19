class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack   = []
        warmer  = [0]*len(temperatures)
        
        i = len(temperatures) - 1
        while i >= 0:
            
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
                
            if stack:
                warmer[i] = stack[-1] - i

            stack.append(i)
                
            i -= 1
            
        return warmer