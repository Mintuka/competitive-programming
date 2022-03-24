class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        subarraySum,size = 0,len(nums)
        
        for left in range(size):
            
            smallest,largest = nums[left],nums[left]
            
            for right in range(left,size):
                
                smallest = min(smallest,nums[right])
                largest  = max(largest,nums[right])
                
                subarraySum += largest - smallest
                
        return subarraySum