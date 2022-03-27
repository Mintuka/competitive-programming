class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = [False]*len(arr)
        while queue:
            popped = queue.popleft()
            if arr[popped] == 0: return True
            if not visited[popped]:
                visited[popped] = True
                if popped - arr[popped] >= 0: queue.append(popped-arr[popped])
                if popped + arr[popped] < len(arr): queue.append(popped+arr[popped])
        return False