class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        #optimize in O(n)
        less    = 0
        indices = 0
        for x in nums:
            if x < target:
                less += 1
            elif x == target:
                indices += 1
        
        return [y + less for y in range(indices)]