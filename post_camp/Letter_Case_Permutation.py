class Solution:
    def __init__(self):
        self.all_possible = []
        self.str = ""
    def backtrack(self, idx, current_str):
        
        if idx == len(self.str):
            self.all_possible.append(''.join(current_str))
            return
        
        current_str.append(self.str[idx])
        self.backtrack(idx+1, current_str)
        current_str.pop()
        
        if self.str[idx].isalpha():
            if 97 <= ord(self.str[idx]) <= 123:
                current_str.append(self.str[idx].upper())
                self.backtrack(idx+1, current_str)
                current_str.pop()
            else:
                current_str.append(self.str[idx].lower())
                self.backtrack(idx+1, current_str)
                current_str.pop()
            
            
    def letterCasePermutation(self, s: str) -> List[str]:
        self.str = s
        self.backtrack(0,[])
        return self.all_possible