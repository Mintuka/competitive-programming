class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        block_sum = [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(1,cols):
                mat[i][j] += mat[i][j-1]
        
        for i in range(rows):
            for j in range(cols):
                start_row, start_col = max(i-k,0),max(j-k,0)
                end_row,end_col = min(i+k,rows-1),min(j+k,cols-1)
                _sum = 0
                for idx in range(start_row,end_row+1):
                    if start_col:
                        _sum += mat[idx][end_col] - mat[idx][start_col-1]
                    else:
                        _sum += mat[idx][end_col]
                block_sum[i][j] = _sum
                
        return block_sum
                