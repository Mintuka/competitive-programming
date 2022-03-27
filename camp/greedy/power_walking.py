n = int(input())
 
for _ in range(n):
    
    size = int(input())
    arr  = list(map(int,input().split()))
    distnict = len(set(arr))
    
    minStrengthList = []
    for k in range(1,size+1):
        minStrength = max(k,distnict)
        minStrengthList.append(str(minStrength))
        
    print(" ".join(minStrengthList))