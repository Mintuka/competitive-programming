class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        rows,cols = len(matrix),len(matrix[0])
        mx = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    left = int(matrix[i][j-1]) if j-1 >= 0 else 0
                    top  = int(matrix[i-1][j]) if i-1 >= 0 else 0
                    diag = int(matrix[i-1][j-1]) if i-1 >= 0 and j-1 >= 0 else 0
                    curr_max = min(left,top,diag)+1
                    mx = max(mx, curr_max)    
                    matrix[i][j] = curr_max
        return mx*mx
                
                