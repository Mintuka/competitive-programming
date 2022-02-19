class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = len(position)
        pos = [[0,0]]*res
        for i in range(res):
            pos[i] = [position[i],speed[i]]
            
        pos = sorted(pos, key=lambda k:k[0], reverse=True)
        
        finishing = [(target - v[0])/v[1] for v in pos]
        
        mxSpeed = finishing[0]
        
        for i in range(1,len(finishing)):
            if finishing[i] <= mxSpeed:
                res -= 1
            else:
                mxSpeed = finishing[i]
            
            
        return res