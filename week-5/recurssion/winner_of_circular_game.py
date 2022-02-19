class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque([v+1 for v in range(n)])
        b = k
        while len(q) > 1:
            if b > 1:
                q.append(q.popleft())
                b -= 1
            else: 
                q.popleft()
                b = k
                
        return q[0]