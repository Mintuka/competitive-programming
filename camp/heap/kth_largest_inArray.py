from heapq import heappush,heappop,heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)): nums[i] = -nums[i]
        heapify(nums)
        while k > 1: 
            heappop(nums)
            k -= 1
        return -nums[0]