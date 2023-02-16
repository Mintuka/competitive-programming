class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        
        ans,size = 0,len(s)
        i = 0
        while i < size:
            if s[i] == 'I' and i+1<size and (s[i+1] == 'V' or s[i+1] == 'X'):
                ans += roman_int[s[i+1]] - roman_int[s[i]]
                i += 1
            elif s[i] == 'X' and i+1<size and (s[i+1] == 'C' or s[i+1] == 'L'):
                ans += roman_int[s[i+1]] - roman_int[s[i]]
                i += 1
            elif s[i] == 'C' and i+1<size and (s[i+1] == 'D' or s[i+1] == 'M'):
                ans += roman_int[s[i+1]] - roman_int[s[i]]
                i += 1
            else:
                ans += roman_int[s[i]]
            i += 1
            
        return ans