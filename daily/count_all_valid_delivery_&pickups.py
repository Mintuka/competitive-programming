class Solution:
    def countOrders(self, n: int) -> int:
        
        def count(n):
            
            if n == 1:
                return 1
            
            subCount = count(n-1)
            
            totalCount = n * (2*n - 1) * subCount
            
            totalCount %= 1000000007
            
            return totalCount
        
        return count(n)