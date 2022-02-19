class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def memoz(N):
            if N in cache: return cache[N]
            if N < 2: return N
            res = memoz(N-1) + memoz(N-2)
            cache[N] = res
            return res
        
        return memoz(n)