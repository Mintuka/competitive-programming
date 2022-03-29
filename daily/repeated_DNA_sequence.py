class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        visited,repeated = set(),set()
        
        index = 9
        
        while index < len(s):
            
            subDNA = "".join(s[index-9:index+1])
            
            if subDNA not in repeated:
                
                if subDNA not in visited:
                    visited.add(subDNA)
                else:
                    repeated.add(subDNA)
                    visited.discard(subDNA)
            
            index += 1
            
        return [subDNA for subDNA in repeated]