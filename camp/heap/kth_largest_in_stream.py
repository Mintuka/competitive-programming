class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        while nums:
            popped = nums.pop()
            if len(self.minHeap) < k: heapq.heappush(self.minHeap,popped)
            elif popped > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap,popped)
        
    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            while len(self.minHeap) < self.k: heapq.heappush(self.minHeap,val)
        elif val > self.minHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap,val)

        return self.minHeap[0]
         


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)