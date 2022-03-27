class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        arrows,index = 0,0
        points.sort()
        
        while index < len(points):
            
            firstEnd = points[index]
            
            while index < len(points) and points[index][0] <= firstEnd[1]:
                
                if firstEnd[1] > points[index][1]:
                    firstEnd = points[index]
                
                index += 1
            
            arrows += 1
            
        return arrows