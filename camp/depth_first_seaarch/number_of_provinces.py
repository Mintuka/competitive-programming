class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(row,visited):
            visited[row] = True
            for j in range(len(isConnected)):
                if isConnected[row][j] == 1 and j != row:
                    isConnected[row][j] = 0
                    dfs(j,visited)
                    
        visited = [False]*len(isConnected)
        provinces = 0
        for i in range(len(isConnected)):  
            if not visited[i]:
                dfs(i,visited)
                provinces += 1

        return provinces