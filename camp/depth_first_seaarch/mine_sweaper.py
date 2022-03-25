def updateBoard(board, click):
    
    def dfs(row,col):
        
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return 'E'
        
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return 'X'
        
        adjacentMines = 0

        if board[row][col] == 'E' and (row,col) not in visited:

            visited.add((row,col))
            
            if row > 0 and (row-1,col) not in visited:
                visited.add((row-1,col)) 
                up = dfs(row-1,col)
                if up == 'M' or up == 'X':
                    adjacentMines += 1
                
                if col > 0 and (row-1,col-1) not in visited:
                    visited.add((row-1,col-1)) 
                    upLeft = dfs(row-1,col-1)
                    if upLeft == 'M' or upLeft == 'X':
                        adjacentMines += 1
                    
                if col+1 < len(board[0]) and (row-1,col+1) not in visited:
                    visited.add((row-1,col+1)) 
                    upRight = dfs(row-1,col+1)
                    if upRight == 'M' or upRight == 'X':
                        adjacentMines += 1
            
            if row+1 < len(board)  and (row+1,col) not in visited:
                visited.add((row+1,col)) 
                down = dfs(row+1,col)
                if down == 'M' or down == 'X':
                    adjacentMines += 1
            
                if col > 0 and (row,col-1) not in visited:
                    visited.add((row,col-1)) 
                    downLeft = dfs(row+1,col-1)
                    if downLeft == 'M' or downLeft == 'X':
                        adjacentMines += 1
                    
                if col+1 < len(board[0]) and (row+1,col+1) not in visited:
                    visited.add((row+1,col+1)) 
                    downRight = dfs(row+1,col+1)
                    if downRight == 'M' or downRight == 'X':
                        adjacentMines += 1
            
            if col > 0 and (row,col-1) not in visited:
                visited.add((row,col-1)) 
                left = dfs(row,col-1)
                if left == 'M' or left == 'X':
                    adjacentMines += 1
            
            if col+1 < len(board[0]) and (row,col+1) not in visited:
                visited.add((row,col+1)) 
                right = dfs(row,col+1)
                if right == 'M' or right == 'X':
                    adjacentMines += 1
            
        board[row][col] = adjacentMines if adjacentMines else 'B'
        
        return board[row][col]
            
    dfs(click[0],click[1])
    
    return board


board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
visited = set()
print(updateBoard(board,click))
# [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]