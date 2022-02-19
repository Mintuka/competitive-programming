class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [0]*N
        dp[-1] = nums[-1]
        
        heap = [(-dp[-1], len(nums)-1)]
        for i in range(N-2, -1, -1):
            lrg, idx = heap[0]
            while idx > min(N-1, i+k):
                heappop(heap) 
                lrg, idx = heap[0]
                
            dp[i] = -lrg+nums[i]
            heappush(heap, (-dp[i], i))
        return dp[0]