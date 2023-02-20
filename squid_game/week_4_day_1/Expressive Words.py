class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            i = j = 0
            while i < len(word) and j < len(s):
                char = word[i]
                count = 0
                while i < len(word) and word[i] == char:
                    count += 1
                    i += 1
                if word[i-1] != s[j]:
                    break
                
                sr = s[j]
                sn = 0
                while j < len(s) and s[j] == sr:
                    sn += 1
                    j += 1
                if (count < sn and sn < 3) or sn < count:
                    break
            else:
                ans += i == len(word) and j == len(s)
        
        return ans