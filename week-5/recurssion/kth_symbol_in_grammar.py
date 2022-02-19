class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        
        p = self.kthGrammar(n-1,k//2 + k%2)
        
        if p:
            return 1 if k%2 else 0
        else:
            return 0 if k%2 else 1