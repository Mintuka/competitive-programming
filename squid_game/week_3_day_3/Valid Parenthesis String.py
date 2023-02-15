class Solution:
    def checkValidString(self, s: str) -> bool:
        openings = []
        stars = []
        
        for idx,char in enumerate(list(s)):
            if char == ')':
                if openings:
                    openings.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                char == '(' and openings.append(idx)
                char == '*' and stars.append(idx)
            
        while openings and stars and stars[-1] > openings[-1]:
            openings.pop()
            stars.pop()
         
        return openings == []