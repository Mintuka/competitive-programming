class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #create stack to hold the max elements
        #create list to save next greater element for each 
        #update the list based on the top of the stack
        stack   = []
        greater = {}
        
        i = len(nums2) - 1
        while i >= 0:
            
            while stack and nums2[i] >= nums2[stack[-1]]:
                stack.pop()
                
            if stack:
                greater[nums2[i]] = nums2[stack[-1]]
            else:
                greater[nums2[i]] = -1

            stack.append(i)
            
            i -= 1
                
        for i,j in enumerate(nums1):
            nums1[i] = greater[j]
            
        return nums1