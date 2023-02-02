class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        difference = sorted([(-growTime[i],plantTime[i],i) for i in range(len(plantTime))])
        
        _max = 0
        plant = 0
        for i in range(len(plantTime)):
            plant += plantTime[difference[i][2]]
            _max = max(_max, plant+growTime[difference[i][2]])
            
        return _max