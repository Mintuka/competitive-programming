class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        mapToIndex,partitions = {},[]
        
        for index in range(len(s)):
            char = s[index]
            mapToIndex[char] = index
            
        index = 0
        while index < (len(s)):
            
            char = s[index]
            left,right = index,mapToIndex[char]
            
            while index < right:
                
                char = s[index]
                right = max(right,mapToIndex[char])
                
                index += 1
                
            partitions.append(right - left + 1)
                
            index += 1
                
        return partitions