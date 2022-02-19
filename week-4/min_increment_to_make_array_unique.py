class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                nums[i] += 1
                cnt += 1
            elif nums[i] < nums[i-1]:
                add = abs(nums[i] - nums[i-1]) + 1
                nums[i] += add
                cnt += add
                
        return cnt