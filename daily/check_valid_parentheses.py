class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        size = len(s)
        possibleChanges,openBracket,closeBracket = 0,0,0
        
        for index in range(size):
            
            if locked[index] == '0':
                possibleChanges += 1
            else:
                if s[index] == '(':
                    openBracket += 1
                else:
                    closeBracket += 1
                    
            if possibleChanges + openBracket < closeBracket:
                return False
        
        
        possibleChanges,openBracket,closeBracket = 0,0,0
        
        for index in range(size-1,-1,-1):
                        
            if locked[index] == '0':
                possibleChanges += 1
            else:
                if s[index] == '(':
                    openBracket += 1
                else:
                    closeBracket += 1
                    
            if possibleChanges + closeBracket < openBracket:
                return False
            
        return False if size%2 else True
    
    