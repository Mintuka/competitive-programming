class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftSearch(nums,left,right,target):
            mid = left + (right - left)//2

            if left > right: return -1
            if nums[mid] == target: 
                first = leftSearch(nums,left,mid-1,target)
                return min(mid,first) if first > -1 else mid
            elif nums[mid] > target: return leftSearch(nums,left,mid-1,target)
            else: return leftSearch(nums,mid+1,right,target)
            
        def rightSearch(nums,left,right,target):
            mid = left + (right - left)//2

            if left > right: return -1
            if nums[mid] == target: 
                last = rightSearch(nums,mid+1,right,target)
                return max(mid,last)
            elif nums[mid] > target: return rightSearch(nums,left,mid-1,target)
            else: return rightSearch(nums,mid+1,right,target)
            
        return [leftSearch(nums,0,len(nums)-1,target),rightSearch(nums,0,len(nums)-1,target)]