class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u,v in adjacentPairs:
            graph[v].add(u)
            graph[u].add(v)
        
        first = float('inf')
        for key,val in graph.items():
            if len(val) == 1:
                first = key
                break
                
        prev = float('inf')
        original = []
        for _ in range(len(adjacentPairs)+1):
            original.append(first)
            nxt = graph[first]
            nxt.discard(prev)
            prev = first
            first = list(nxt)[0] if nxt else 0
        return original
            
        