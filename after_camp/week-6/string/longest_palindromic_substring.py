class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        size,longest = len(s),(0,0)
        index = 0
        
        while index < size:
        
            left,right = index,index
            
            while left-1 >= 0 and right+1 < size and s[left-1] == s[right+1]:
                
                left  -= 1
                right += 1
            
            start,end = longest
            if end - start < right - left:
                longest = (left,right)
            
            
            left,right = index+1,index
            
            while left-1 >= 0 and right+1 < size and s[left-1] == s[right+1]:
                
                left  -= 1
                right +=1
               
            start,end = longest
            if end - start < right - left:
                longest = (left,right)
            
            
            index += 1
            
        start,end = longest 
        
        return s[start:end+1]