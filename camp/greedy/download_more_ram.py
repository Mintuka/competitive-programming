n = int(input())
 
for _ in range(n):
    
    size,available  = list(map(int,input().split()))
    require,provide = list(map(int,input().split())),list(map(int,input().split()))
    
    rams = [(require[i],provide[i]) for i in range(size)]
    rams.sort()
    
    while rams and available >= rams[0][0]:
        popped = rams.pop(0)
        available += popped[1]
        
    print(available)