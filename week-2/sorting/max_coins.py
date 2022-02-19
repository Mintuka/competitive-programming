class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins = 0
        i = len(piles)  - 2
        j = len(piles) // 3
        while j > 0:
            coins += piles[i]
            i -= 2
            j -= 1
            
        return coins