class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left  = [0]*n
        right = [0]*n
        #smallest element on the left side
        stack = deque()
        i = 0
        while i < n:
            while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()

            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
                    
            i += 1
        #smallest element on the right side
        stack = deque()
        i = n - 1
        while i >= 0:
            while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                    
            right[i] = stack[-1] - 1 if stack else n - 1
            stack.append(i)
            
            i -= 1
            
        #max rectangle
        mx = 0
        for i in range(n):
            area = heights[i] * (right[i] - left[i] + 1)
            mx = max(mx,area)
            
        return mx