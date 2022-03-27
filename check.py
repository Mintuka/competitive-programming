from array import array
from math import pow, floor, log10
from collections import deque

def kthPalindrome(queries, intLength):

    combinations = intLength // 2 + intLength % 2
    maxPalindrom = pow(10,combinations - 1) * 9
    palindromes = []
    
    for query in queries:
        
        palindrome = deque()
        
        if query > maxPalindrom:
            palindromes.append(-1)
        else:
            
            for digit in range(intLength):
                inner = (query // pow(10,digit) % 10) - 1
                if inner == -1: 
                    palindrome.appendleft(9)
                else:
                    palindrome.appendleft(int(inner))
                
            palindrome[0] += 1
            size = len(palindrome)
            
            if size%2:
                for index in range(size-2,-1,-1):
                    palindrome.append(palindrome[index])
            else:
                for index in range(size-1,-1,-1):
                    palindrome.append(palindrome[index])
            
        
        palindrome and palindromes.append(int("".join([str(num) for num in palindrome])))
        
    return palindromes

arr = [1,2,3,4,5,90]
len = 3
kthPalindrome(arr,len)