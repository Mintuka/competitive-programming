class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        newFlowers = 1 if len(flowerbed) < 3 and n == 1 and flowerbed[0] == flowerbed[-1] == 0 else 0
        
        start,nxt = 0,2
        
        if len(flowerbed) > 2: 
            if flowerbed[0] == flowerbed[1] == 0: 
                flowerbed[0] = 1
                newFlowers += 1
            if flowerbed[-1] == flowerbed[-2] == 0:
                flowerbed[-1] = 1
                newFlowers += 1
        
        while nxt < len(flowerbed):
            
            if flowerbed[start + 1] == flowerbed[start] == flowerbed[nxt] == 0:
                flowerbed[start + 1] = 1
                newFlowers += 1
            
            start,nxt = start+1,nxt+1
        
        return newFlowers >= n