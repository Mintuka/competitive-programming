from heapq import heappush,heappop,heapify
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        size,i = len(heights),0
        minHeap,bricksUsed = [],0
        while i < size-1:
            height = heights[i] - heights[i+1]
            if height < 0:                
                if len(minHeap) < ladders:heappush(minHeap,-height)
                else:
                    heappush(minHeap,-height)
                    if bricksUsed + (minHeap[0]) <= bricks: bricksUsed += heappop(minHeap)
                    else: break
            
#             if height < 0:heappush(minHeap,-height)
#             if len(minHeap) > ladders: bricksUsed += heappop(minHeap)
#             if bricksUsed > bricks: break
#             i += 1
            
            i += 1
            
        return i
        
        