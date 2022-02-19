class Solution:
    
    def findKthBit(self, n: int, k: int) -> str:
        def construct(s,n):
            if n == 0: return s
            inv = invert(s)
            return construct(s + "1" + inv,n-1)
    
        def invert(s):
            inv = deque()
            for v in s: inv.append("0") if v == "1" else inv.append("1")
            return "".join(inv)[::-1]
        
        return construct("0",n)[k-1]