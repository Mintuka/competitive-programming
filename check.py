def eventualSafeNodes(graph):
    
    #filter terminal nodes (empty lists)
    #check if all neighbours of non terminal nodes are terminl nodes
    
    size      = len(graph)
    terminals = set()
    safe      = set()
    visited   = [False]*size
    
    for i in range(size):
        
        if not graph[i]:
            terminals.add(i)
    
    for i  in range(size):
        
        isPossible = False
        neighbours = 0
        for neighbour in graph[i]:
            
            isPossible = dfs(neighbour,terminals,visited,graph,isPossible)
            if isPossible:
                neighbours += 1
        
        if neighbours == len(graph[i]):
            safe.add(i)
            
    return safe

def dfs(node,terminals,visited,graph,isPossible):
    
    if node in terminals:
        return True
    
    visited[node] = True
    isSafe = False
    
    for neighbour in graph[node]:
        
        if not visited[neighbour]:
            isSafe = isPossible and dfs(neighbour,terminals,visited,graph,isSafe)
            
    visited[node] = False
    
    return isSafe


graph = [[],[0,2,3,4],[3],[4],[]]
eventualSafeNodes(graph)



        