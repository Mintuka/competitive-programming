class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(node, cost, dest):
            if node not in graph:
                return -1
            visited.add(node)

            if node == dest:
                return cost
            res = -1
            for neg,val in graph[node]:
                if neg not in visited:
                    res = max(res,dfs(neg, cost*val, dest))
            return res
        
        graph = defaultdict(list)
        for idx in range(len(equations)):
            u,v = equations[idx]
            cost = values[idx]
            graph[u].append((v,cost))
            graph[v].append((u,1/cost))
            
        result = [-1 for i in range(len(queries))]
        for idx,(x,y) in enumerate(queries):
            visited = set()
            ans = dfs(x, 1, y)
            result[idx] = ans
        
        return result