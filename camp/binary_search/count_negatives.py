class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def search(sorted,left,right):
            if left > right: return len(sorted)-left
            mid = left + (right - left)//2
            if sorted[mid] >= 0: return search(sorted,mid+1,right)
            else: return search(sorted,left,mid-1)
            
        negatives = 0
        for list in grid:
            left,right = 0,len(grid[0])-1
            negatives += search(list,left,right)
            
        return negatives
            