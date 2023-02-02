class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l = whites = 0
        
        for r in range(len(blocks)):
            if r-l < k:
                if blocks[r] == 'W':
                    whites += 1
                _min = whites
                continue
            if blocks[r] == 'W':
                whites += 1

            if blocks[l] == 'W':
                whites -= 1

            l += 1
            _min = min(_min, whites)
            
        return _min