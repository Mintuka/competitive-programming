class Solution:
    
    def __init__(self):
        self.parentheses = []
    
    def generateParenthesis(self, n: int) -> List[str]:

        self.findAll(n, 0, 0, [])
        return self.parentheses
        
    def findAll(self, n, openings, closings, parenthes):
        if openings == n and closings == n:
            self.parentheses.append(''.join(parenthes))
        # print(parenthes)
        if openings < n:
            parenthes.append('(')
            self.findAll(n, openings+1, closings, parenthes)
            parenthes.pop()
            
        if closings < n and closings < openings:
            parenthes.append(')')
            self.findAll(n, openings, closings+1, parenthes)
            parenthes.pop()