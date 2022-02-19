class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = deque([0])
        mn = deque([0])
        size,left = 1,0
        i = 1
        while i < len(nums):
            while mx and abs(nums[i] - nums[mx[0]]) > limit:    
                left = max(left,mx[0]+1)
                mx.popleft()

            while mn and abs(nums[i] - nums[mn[0]]) > limit:    
                left = max(left,mn[0]+1)            
                mn.popleft()

            size = max(size,abs(i - left + 1))  
            
            while mx and nums[mx[-1]] < nums[i]:    
                mx.pop()            
            mx.append(i)
               
            while mn and nums[mn[-1]] > nums[i]:    
                mn.pop()
            mn.append(i)
            
            i += 1

        return size