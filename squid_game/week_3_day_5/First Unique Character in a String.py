class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = defaultdict(list)
        alphabets = []
        for i,char in enumerate(s):
            if char not in chars:
                alphabets.append(char)
                chars[char] = [1,i]
            else:
                chars[char][0] += 1
        
        for char in alphabets:
            if chars[char][0] == 1:
                return chars[char][1]
                
        return -1