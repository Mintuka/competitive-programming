class AllOne:

    def __init__(self):
        self.dict = defaultdict(int)        
        self.minHeap = []
        self.maxHeap = []
        
    def inc(self, key: str) -> None:
        self.dict[key] += 1
        heappush(self.minHeap, (self.dict[key], key))
        heappush(self.maxHeap, (-self.dict[key], key))

    def dec(self, key: str) -> None:
        self.dict[key] -= 1
        if self.dict[key] < 1:
            del self.dict[key]
            return
        heappush(self.minHeap, (self.dict[key], key))
        heappush(self.maxHeap, (-self.dict[key], key))
        
    def getMaxKey(self) -> str:
        while self.maxHeap and (self.maxHeap[0][1] not in self.dict or self.maxHeap[0][0] != -self.dict[self.maxHeap[0][1]]):
            heappop(self.maxHeap)
        if self.maxHeap:
            return self.maxHeap[0][1]
        return ""
    
    def getMinKey(self) -> str:
        while self.minHeap and (self.minHeap[0][1] not in self.dict or self.minHeap[0][0] != self.dict[self.minHeap[0][1]]):
            heappop(self.minHeap)
        if self.minHeap:
            return self.minHeap[0][1]
        return ""