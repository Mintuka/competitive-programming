class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def search(row,col,target):
            
            if image[row][col] == target:
                image[row][col] = newColor
                if col < len(image[0])-1: search(row,col+1,target)
                if col > 0: search(row,col-1,target)
                if row > 0: search(row-1,col,target)
                if row < len(image)-1: search(row+1,col,target)
        
        target = image[sr][sc]                   
        newColor != image[sr][sc] and search(sr,sc,target)
        return image