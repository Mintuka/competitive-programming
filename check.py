def shipWithinDays(weights,days):
    
    def calcDays(capacity,packages):
        
        index,Ddays = 0,0
        left,right = 0,1
        while right < len(packages):
            
            while right < len(packages) and packages[right] - packages[left] <= capacity:
                right += 1
            
            left = right - 1
            Ddays += 1
            
        return Ddays
    
    left,right = max(weights),sum(weights)
    prefixSum = [0,*weights]
    for i in range(1,len(prefixSum)): 
        prefixSum[i] += prefixSum[i-1]
    
    while left < right:
        
        capacity = left + (right - left)//2
        
        Ddays = calcDays(capacity,prefixSum)
        
        if Ddays <= days:
            right = capacity
        else:
            left = capacity + 1
        
        
    return left

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights,days))