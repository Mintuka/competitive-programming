class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = int(math.pow(10,9) + 7)
        def logPow(v,p,mod):
            if p == 0: return 1
            pow = logPow(v,p//2,mod)
            pow = pow * pow
            pow %= mod
            if p%2: pow *= v
            pow %= mod
            
            return pow
        p4 = n//2
        p5 = p4 + (n%2)

        return int(logPow(5,p5,mod) * logPow(4,p4,mod)) % mod