from heapq import heappop,heappush
class MedianFinder:

    def __init__(self):
        self.minHeap = []        
        self.maxHeap = []
    def addNum(self, num: int) -> None:
        if len(self.maxHeap) > len(self.minHeap):
            if num < -self.maxHeap[0]:
                heappush(self.minHeap,-heappop(self.maxHeap))
                heappush(self.maxHeap,-num)
            else: heappush(self.minHeap,num)
        elif len(self.maxHeap) == len(self.minHeap):
            if self.maxHeap and num > -self.maxHeap[0] : heappush(self.minHeap,num)
            else: heappush(self.maxHeap,-num)
        else:
            if num > self.minHeap[0]:
                heappush(self.maxHeap,-heappop(self.minHeap))
                heappush(self.minHeap,num)
            else: heappush(self.maxHeap,-num)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap): return -self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap): return self.minHeap[0]
        else: return (self.minHeap[0] - self.maxHeap[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()