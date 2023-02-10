class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        size = len(img1)
        count = [[0 for i in range(2*size+1)] for j in range(2*size+1)]
        
        for i in range(size):
            for j in range(size):
                if img1[i][j] == 1:
                    for r in range(size):
                        for c in range(size):
                            if img2[r][c] == 1: 
                                count[i-r+size][j-c+size] += 1                         

        largest = 0
        for i in range(len(count)):
            for j in range(len(count)):
                largest = max(largest, count[i][j])
        return largest