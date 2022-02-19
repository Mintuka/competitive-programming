class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 1000000007
        def pow(x,n):
            if n == 0: return 1
            val = pow(x,n//2)
            val *= val
            val %= mod
            if n%2: val *= x
            val %= mod
            return val
        
        x = (2**p) - 1
        return int((pow(x-1,x//2)%mod) * (x%mod)) % mod