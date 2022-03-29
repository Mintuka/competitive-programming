class Solution:
    
    def findMax(self,frequency,maxValues):
        
        for key in frequency.keys():

            if frequency[key] > frequency[maxValues[0]]:
                maxValues[0],maxValues[1] = key,maxValues[0]

            elif frequency[key] > frequency[maxValues[1]]:
                maxValues[1] = key        
        
        return maxValues
    
    def minimumOperations(self, nums: List[int]) -> int:
        
        oddIndices, evenIndices = defaultdict(int),defaultdict(int)
        evenMax,oddMax = [0,0],[0,0]
        minOperations = len(nums)

        for index in range(len(nums)):

            if index % 2:

                oddIndices[nums[index]] += 1

            else:

                evenIndices[nums[index]] += 1

        oddIndices[0],evenIndices[0] = 0,0

        evenMax = self.findMax(evenIndices,evenMax)
        oddMax  = self.findMax(oddIndices,oddMax)

        if evenMax[0] != oddMax[0]:

            minOperations = len(nums) - evenIndices[evenMax[0]] - oddIndices[oddMax[0]]

        else:
            
            maxOne = evenIndices[evenMax[0]] + oddIndices[oddMax[1]]
            maxTwo = evenIndices[evenMax[1]] + oddIndices[oddMax[0]]
            maxThree = evenIndices[evenMax[1]] + oddIndices[oddMax[1]]
            
            minOperations = len(nums) - max(maxOne,maxTwo,maxThree)

        return minOperations