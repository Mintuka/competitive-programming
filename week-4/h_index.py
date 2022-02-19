class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        i = len(citations) - 1
        while i >= 0:
            if citations[i] > h and citations[i] > 0:
                h += 1
            i -= 1
                            
        return h