class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        unique = sorted(set(changed))
        count = Counter(changed)
        original = []
        if 0 in unique and count[0]%2:
            return []

        for num in unique:
            doubled = num*2
            
            while doubled in count and num in count:
                count[doubled] -= 1
                count[num] -= 1
                original.append(num)
                if count[num] == 0:
                    del count[num]
                if count[doubled] == 0:
                    del count[doubled]
            
            if num in count:
                return []
                
        return original