class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left  = [0]*n
        right = [height[-1]]*n
        
        #left largest block
        stack = deque([height[0]])
        for i in range(1,n):
            left[i] = stack[-1]
            if height[i] > stack[-1]: stack.append(height[i])
        #right largest block                
        stack = deque([height[-1]])
        for i in range(n-1,0,-1):
            right[i] = stack[-1]
            if height[i] > stack[-1]: stack.append(height[i])
        
        contain = 0
        for i in range(n):
            if min(left[i],right[i]) - height[i] > 0:
                contain += min(left[i],right[i]) - height[i]
            
        return contain