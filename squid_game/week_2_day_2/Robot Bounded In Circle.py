class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        x,y = 0,0        
        direction = (0,1)
        
        for move in instructions:
            if move == 'G':
                x,y = x+direction[0],y+direction[1]
            elif move == 'L':
                direction = (-direction[1],direction[0])
            else:
                direction = (direction[1],-direction[0])
            
        if x == 0 and y == 0:
            return True
        if direction != (0,1):
            return True
        return False