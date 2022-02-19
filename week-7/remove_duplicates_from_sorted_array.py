class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,position = 0,0
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                position += 1
                nums[position ] = nums[i+1]
                
            i += 1
            
        return position+1