from math import ceil,pow,log10
from string import digits
def kthPalindrome(queries, intLength):

    palindromes = []
    
    for query in queries:
        
        nthPalindrome = pow(10,ceil(intLength/2) - 1) * 9
        if query <= nthPalindrome:

            digits = ceil(log10(query))            
            halfPalindrome = []
            end = ceil(intLength/2)

            if digits == end:
                halfPalindrome.append(int(query // pow(10,end-1))%10)
            else:
                halfPalindrome.append(1)

            for index in range(end-2,-1,-1):
                value = int(query // pow(10,index))%10 - 1
                if value == -1: 
                    value = 9
                halfPalindrome.append(value)
                
            halfPalindrome = [str(num) for num in halfPalindrome]
            rightPalindrome = halfPalindrome[::-1]
            print(rightPalindrome)
            
            num = ""
            if intLength%2:
                num = "".join([*halfPalindrome,*[rightPalindrome[i] for i in range(len(rightPalindrome)) if i > 0]])
            else:
                num = "".join([*halfPalindrome,*rightPalindrome])
                
            palindromes.append(int(num))
        else:
            
            palindromes.append(-1)
            
    return palindromes

queries = [1,2,3,4,5,90] 
intLength = 3
print(kthPalindrome(queries,intLength))