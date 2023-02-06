class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1,0)])
        visited = set()
        
        while queue:
            position,speed,steps = queue.popleft()
            if (position,speed) in visited:
                continue
            visited.add((position,speed))
            if position == target:
                return steps
            if speed > 0:
                queue.append((position+speed, speed*2, steps+1))
                queue.append((position, -1, steps+1))
            else:
                queue.append((position+speed, speed*2, steps+1))
                queue.append((position, 1, steps+1))