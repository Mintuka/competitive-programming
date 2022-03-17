class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency: frequency[num] += 1
            else: frequency[num] = 1
                
        maxHeap = []
        for num in frequency: heapq.heappush(maxHeap,(-frequency[num],num))
        
        sortedChars = []
        while k > 0:
            sortedChars.append(maxHeap[0][1])
            heapq.heappop(maxHeap)
            k -= 1
            
        return sortedChars