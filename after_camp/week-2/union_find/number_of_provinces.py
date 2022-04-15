class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        size        = len(isConnected)
        connections = [1]*size
        parent      = [i for i in range(size)]
        
        def find(u):
            
            while parent[u] != u:
                u = parent[u]
        
            return u
        
        def union(u,v):
            
            u,v = find(u),find(v)
            
            if u != v:
                
                if connections[u] >= connections[v]:
                    connections[u] += connections[v]
                    parent[v] = u
                else:
                    connections[v] += connections[u]
                    parent[u] = v
                    
        for i in range(size):
            for j in range(i+1,size):
                
                if isConnected[i][j] == 1:
                    union(i,j)
                    
        
        provinces = 0
        for i in range(size):
            if parent[i] == i:
                provinces += 1
                
        return provinces