class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        left,right = 1,min(time)*totalTrips
        def timeCalculator(mid):
            trips = 0
            for i in range(len(time)): trips += mid//time[i] 
            return trips
        
        def search(left,right):
            mid = left + (right - left)//2
            if left > right: return left
            if timeCalculator(mid) >= totalTrips: return search(left,mid-1) 
            else: return search(mid+1,right)
            
        return search(left,right-1)
        
        