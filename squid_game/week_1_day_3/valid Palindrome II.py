class Solution:
    def validPalindrome(self, s: str) -> bool:

        left,right = 0,len(s)-1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                L1,R1 = left+1,right
                L2,R2 = left,right-1
                return s[L1:R1+1] == s[L1:R1+1][::-1] or s[L2:R2+1] == s[L2:R2+1][::-1]
        return True
                