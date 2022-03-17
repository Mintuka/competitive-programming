from heapq import heappush,heappop,heapify
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for array in matrix:
            for num in array: minHeap.append(num)
        heapify(minHeap)
        
        while k > 1: 
            heappop(minHeap)
            k -= 1
        return minHeap[0]