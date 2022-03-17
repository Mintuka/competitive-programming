from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        size = len(nums)
        left,right = 1,max(nums)
        
        nums.sort()
        
        while left < right:
            
            mid = left + (right - left)//2
            
            divisionsSum = 0
            for i in range(size):
                divisionsSum += ceil(nums[i]/mid)
                
            if divisionsSum <= threshold:
                right = mid
            else:
                left = mid + 1
                
        return int(left)
                
                
        