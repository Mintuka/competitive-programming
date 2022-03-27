class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        change = False
        i = 0
        palindrome = list(palindrome)
        
        while i < len(palindrome) and not change:
        
            if palindrome[i] != 'a' and len(palindrome)//2 != i:
                palindrome[i] = 'a'
                palindrome = "".join(palindrome)
                change = True  

            i += 1

        if len(palindrome) > 1 and not change:
            palindrome[-1] = 'b'    
            palindrome = "".join(palindrome)
            change = True
        
        return palindrome if change else ""