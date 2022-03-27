from collections import defaultdict

def characterReplacement(s, k):
    
    characters = defaultdict(int)
    size,operations = len(s),k
    longest,left,right = 0,0,0
    
    while right < size:
        
        characters[s[right]] += 1
        
        if operations > 0 and s[left] != s[right]:
            operations -= 1

        longest = max(longest,right - left + 1)    
        
        if operations == 0 and s[left] != s[right]:
            operations -= 1
        
        while operations < 0 and left < right :
            
            characters[s[left]] -= 1
            operations = right - left - characters[s[left]]
            left += 1

        right += 1
    
    
        
    return longest

s = "AABABBA" 
k = 1
characterReplacement(s,k)