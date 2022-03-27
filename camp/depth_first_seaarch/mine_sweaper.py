class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def countAdjacentMines(row,col):
            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
            count = 0
            for i in range(row-1,row+2):
                for j in range(col-1,col+2):
                    if i >=0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] == 'M':
                        count += 1
                        
            return count
        
        def dfs(row,col):
            
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return board
            
            if board[row][col] == 'E':
                
                count = countAdjacentMines(row,col)
                if count:
                    board[row][col] = str(count)
                else:
                    board[row][col] = 'B'
                    
                    for i in range(row-1,row+2):
                        for j in range(col-1,col+2):
                            if i >=0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] != 'B':
                                dfs(i,j)
            return board
                
        return dfs(*click)
        