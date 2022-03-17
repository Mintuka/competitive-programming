class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        size,smallestNums = m*n,0
        left,right = 1,size
        while left < right:
            mid = left + (right-left)//2
            smallestNums = 0
            for i in range(1,m+1): smallestNums += min(mid//i,n)
            if smallestNums >= k: right = mid
            else: left = mid+1
                
        return left