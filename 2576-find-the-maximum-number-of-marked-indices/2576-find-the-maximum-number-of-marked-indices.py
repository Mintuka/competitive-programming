class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        
        size = len(nums)
        nums.sort()
        marked = 0
        left  = 0
        
        for right in range(size - size//2, size):
            if 2*nums[left] <= nums[right]:
                marked += 2
                left += 1
                
        return marked