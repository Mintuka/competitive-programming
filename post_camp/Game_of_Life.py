class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                lives = 0
                for dx,dy in directions:
                    if 0 <= row+dx < len(board) and 0 <= col+dy < len(board[0]):
                        if abs(board[row+dx][col+dy]) == 1:
                            lives += 1
                if not (2 <= lives <= 3) and board[row][col] == 1:
                    board[row][col] = -1
                if lives == 3 and board[row][col] == 0:
                    board[row][col] = 2
                
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 2:
                    board[row][col] = 1
                if board[row][col] == -1:
                    board[row][col] = 0
                    
        return board
        