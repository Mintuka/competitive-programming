class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row,col):
            if board[row][col] == "O":
                board[row][col] = "1"
                if row > 0: dfs(row-1,col)
                if row < len(board)-1: dfs(row+1,col)
                if col > 0: dfs(row,col-1)
                if col < len(board[0])-1: dfs(row,col+1)
        
        for i in range(len(board)):
            dfs(i,0)
            dfs(i,len(board[0])-1)
        for j in range(len(board[0])):
            dfs(0,j)
            dfs(len(board)-1,j)
        print(board)    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O": board[i][j] = "X"
                elif board[i][j] == "1": board[i][j] = "O"
                    
        return board