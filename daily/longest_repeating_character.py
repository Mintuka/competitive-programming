class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        characters = defaultdict(int)
        size,operations = len(s),k
        longest,left,right = 0,0,0
        frequent = [s[0],1]
        
        while right < size:
            
            characters[s[right]] += 1
            
            if frequent[1] <= characters[s[right]]:
                frequent = [s[right],characters[s[right]]]
            
            # window = right - left + 1
            while (right - left + 1) - frequent[1] > k:
                characters[s[left]] -= 1
                if s[left] == frequent[0]:
                    frequent[1] -= 1
                left += 1
                
            longest = max(longest,right - left + 1)
            
            right += 1
            
        return longest