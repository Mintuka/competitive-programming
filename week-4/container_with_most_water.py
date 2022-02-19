class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        cnt,area = 0,0
        while l < r:
            area = min(height[l],height[r]) * (r-l)
            cnt = max(cnt,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return cnt