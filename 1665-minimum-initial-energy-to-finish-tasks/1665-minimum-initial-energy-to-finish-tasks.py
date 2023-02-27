class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        def isMin(cost, arr):
            for ac,mn in arr:
                if cost < mn:
                    return False
                cost -= ac
            return True
        
        l = r = 0
        for x,y in tasks:
            r += y
        tasks.sort(key=lambda x:x[1], reverse=True)
        tasks.sort(key=lambda x:x[1] - x[0], reverse=True)
           
        while l <= r:
            mid = (l+r)//2
            isEnough = isMin(mid, tasks)
            if isEnough:
                r = mid-1
            else:
                l = mid+1
        
        if isMin(l-1, tasks):
            return l-1
        return l
            