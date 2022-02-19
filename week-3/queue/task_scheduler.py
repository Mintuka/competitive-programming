class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-c for c in freq.values()]
        heapq.heapify(maxHeap)
        
        time,queue = 0,deque()
        while maxHeap or queue:
            time +=1
            if maxHeap: 
                task = 1 + heapq.heappop(maxHeap)
                if task: queue.append([task,time+n])
            if queue and queue[0][1] == time: 
                heapq.heappush(maxHeap,queue.popleft()[0])
                
        return time