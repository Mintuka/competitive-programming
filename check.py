from collections import defaultdict

def minimumOperations(nums):
    
    oddIndices, evenIndices = defaultdict(int),defaultdict(int)
    evenMax,oddMax = [0,0],[0,0]
    minOperations = len(nums)
    
    for index in range(len(nums)):
        
        if index % 2:
            
            oddIndices[nums[index]] += 1

        else:
            
            evenIndices[nums[index]] += 1
            
    oddIndices[0],evenIndices[0] = 0,0
    
    for key in oddIndices.keys():

        if oddIndices[key] > oddIndices[oddMax[0]]:
            oddMax[0],oddMax[1] = key,oddMax[0]

        elif oddIndices[key] > oddIndices[oddMax[1]]:
            oddMax[1] = key

    for key in evenIndices.keys():

        if evenIndices[key] > evenIndices[evenMax[0]]:
            evenMax[0],evenMax[1] = key,evenMax[0]
            
        elif evenIndices[key] > evenIndices[evenMax[1]]:
            evenMax[1] = key
                
    if evenMax[0] != oddMax[0]:
        
        minOperations = len(nums) - evenIndices[evenMax[0]] - oddIndices[oddMax[0]]
        
    else:
        
        if evenIndices[evenMax[0]] > oddIndices[oddMax[0]]:

            minOperations = len(nums) - evenIndices[evenMax[0]] - oddIndices[oddMax[1]]

        elif evenIndices[evenMax[0]] == oddIndices[oddMax[0]]:

            minOperations = len(nums) - evenIndices[evenMax[0]] - max(evenIndices[evenMax[1]],oddIndices[oddMax[1]])

        else:

            minOperations = len(nums) - evenIndices[evenMax[1]] - oddIndices[oddMax[0]]
        
                    
    return minOperations

print(minimumOperations([1,2,2,2,2]))