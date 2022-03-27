n = int(input())
 
for _ in range(n):
    
    size = int(input())
    arr  = list(map(int,input().split()))
    arr.sort()
    
    for i in range(1,len(arr)): arr[i] += arr[i-1]
    
    k,r = 1,size-1
    while k < size//2 + 1:
        
        redSum  = arr[r] - arr[r-k]
        blueSum = arr[k]
        
        if redSum > blueSum: 
            print("YES")
            break
        
        k += 1
        
    else: 
        print("NO")