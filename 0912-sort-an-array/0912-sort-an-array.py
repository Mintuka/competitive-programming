class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        mn = abs(min(nums))
        for i in range(len(nums)):
            nums[i] += mn
        
        size = abs(max(nums)) + mn + 1
        count = [0 for _ in range(size)]
        
        for num in nums:
            new_mn = num
            count[new_mn] += 1
         
        for i in range(1,len(count)):
            count[i] += count[i-1]
        
        res = [0 for i in range(len(nums))]
        
        for idx,val in enumerate(nums):
            res[count[val]-1] = val
            count[val] -= 1
        
        for i in range(len(res)):
            res[i] -= mn
            
        return res