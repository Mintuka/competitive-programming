class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def search(citations,left,right):
            mid = left + (right - left)//2
            if left > right: return len(citations) - left
            
            hIndex = len(citations) - mid
            if hIndex == citations[mid]: return citations[mid]
            elif hIndex > citations[mid]: return search(citations,mid+1,right)
            else: return search(citations,left,mid-1)
            
        return search(citations,0,len(citations)-1)