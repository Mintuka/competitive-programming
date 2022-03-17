class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(row,left,right):
            if left > right: return False
            mid = left + (right-left)//2
            if matrix[row][mid] == target: return True
            elif matrix[row][mid] < target: return search(row,mid+1,right)
            else: return search(row,left,mid-1)
        
        for i in range(len(matrix)):
            if matrix[i][len(matrix[0])-1] > target: return search(i,0,len(matrix[0])-1)
            elif matrix[i][len(matrix[0])-1] == target: return True
                
                