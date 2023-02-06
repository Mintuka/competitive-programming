from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.x = defaultdict(set)
        self.y = defaultdict(set)
        self.countP = defaultdict(int)

    def add(self, point) -> None:
        x,y = point
        self.x[x].add(y)
        self.y[y].add(x)
        self.countP[(x,y)] += 1
        
    def count(self, point) -> int:
        x,y = point
        ys = self.x[x]
        count_ = 0
        for py in ys:
            gap = abs(y - py)
            if py > y:
                if x+gap in self.y[py] and x+gap in self.y[y]:
                    count_ += self.countP[(x,py)] + self.countP[(x+gap,py)] + self.countP[(x+gap,y)]
                if x-gap in self.y[py] and x-gap in self.y[y]:
                    count_ += self.countP[(x,py)] + self.countP[(x-gap,py)] + self.countP[(x-gap,y)]
            if py < y:
                if x+gap in self.y[y] and x+gap in self.y[y-gap]:
                    count_ += self.countP[(x,y-gap)] + self.countP[(x+gap,y-gap)] + self.countP[(x+gap,y)]
                if x-gap in self.y[y-gap] and x-gap in self.y[y]:
                    count_ += self.countP[(x,y-gap)] + self.countP[(x-gap,y-gap)] + self.countP[(x-gap,y)]
        count_ *= (self.countP[(x,y)]+1)
        return count_

obj = DetectSquares()
obj.add([3,10])
obj.add([11,2])
obj.add([3,2])
obj.count([11,10])
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)