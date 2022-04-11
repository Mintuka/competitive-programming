class Solution:
    def countVowels(self, word: str) -> int:
        
        size   = len(word)
        vowels = set("aeiou")
#iterative approach (Bottom - Up)
        current,sumOfVowels = 0,0
        
        for i in range(size):
            
            if word[i] in vowels:
                
                current += i + 1
                
            sumOfVowels += current
            
        return sumOfVowels
#recursive approach (Top - Down)
#         @lru_cache(None)
#         def dp(i):
            
#             if i == 0:
#                 if word[i] in vowels:
#                     return (1,1)
#                 else:
#                     return (0,0)

#             current,sumOfVowels = dp(i-1)
            
#             if word[i] in vowels:
                
#                 current += i + 1
                
#             sumOfVowels += current

#             return (current,sumOfVowels)
            
#         return dp(size-1)[1]