class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(n):
            if n == 0: return 1
            ans = self.myPow(x,n//2)
            ans = ans * ans * (x if n%2 else 1)        
            return ans
        
        if n < 0: return 1/pow(abs(n))
        return pow(n)