class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left,right):
            
            mid = left + (right - left)//2
            
            if left > right: return -1
            
            if nums[mid] == target: 
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return binarySearch(left,mid-1)
                else:
                    return binarySearch(mid+1,right)
            else:
                if nums[mid] < target <= nums[right]:
                    return binarySearch(mid+1,right)
                else:
                    return binarySearch(left,mid-1)
            
                
        return binarySearch(0,len(nums)-1)