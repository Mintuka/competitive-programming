class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        L,R = 0,len(nums)-1
        minSum = [0]*(len(nums)//2)
        #sort nums
        nums.sort()
        while L < len(nums)//2:
            minSum[L] = nums[L] + nums[R]
            L += 1
            R -= 1
        #sort minSum
        minSum.sort()
        
        return minSum[-1]