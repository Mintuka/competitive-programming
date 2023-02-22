class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = list(s)
        steps = 0
        for _ in range(len(s)):
            isSwaped = False
            i = 0
            while i < len(s):
                if  i+1 < len(s) and s[i] == "0" and s[i+1] == "1":
                    s[i],s[i+1] = s[i+1],s[i]
                    isSwaped = True
                    i += 1
                i += 1
            if isSwaped:
                steps += 1
        return steps
            
                
                