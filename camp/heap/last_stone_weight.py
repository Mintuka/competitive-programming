class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            difference = -heapq.heappop(maxHeap) - (-heapq.heappop(maxHeap))
            if difference > 0: heapq.heappush(maxHeap,-difference)
            
        return -maxHeap[0] if maxHeap else 0
        