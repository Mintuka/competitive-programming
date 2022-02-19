class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return spiral(matrix).spr
        
class spiral:
    def __init__(self,matrix):
        self.matrix = matrix
        self.n,self.e = 0,0
        self.w,self.s = len(matrix[0]) - 1,len(matrix) - 1
        self.spr = deque()
        self.cnt = (self.w+1) * (self.s+1)
        self.lr()

        self.s -= 1
    def lr(self):
        if self.cnt == 0: return
        for i in range(self.e,self.w+1):
            self.spr.append(self.matrix[self.n][i])
            self.cnt -= 1            
        self.n += 1
        self.td()

    def td(self):
        if self.cnt == 0: return
        for i in range(self.n,self.s+1):
            self.spr.append(self.matrix[i][self.w])
            self.cnt -= 1
        self.w -= 1
        self.rl()

    def rl(self):
        if self.cnt == 0: return
        for i in range(self.w,self.e-1,-1):
            self.spr.append(self.matrix[self.s][i])
            self.cnt -= 1
        self.s -= 1
        self.dt()

    def dt(self):
        if self.cnt == 0: return
        for i in range(self.s,self.n-1,-1):
            self.spr.append(self.matrix[i][self.e])
            self.cnt -= 1
        self.e += 1
        self.lr()