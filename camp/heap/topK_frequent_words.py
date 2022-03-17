class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}
        for word in words:
            if word in frequency: frequency[word] += 1
            else: frequency[word] = 1
                
        maxHeap = []
        for word in frequency: heapq.heappush(maxHeap,(-frequency[word],word))
        
        sortedChars = []
        while k > 0:
            sortedChars.append(maxHeap[0][1])
            heapq.heappop(maxHeap)
            k -= 1
            
        return sortedChars