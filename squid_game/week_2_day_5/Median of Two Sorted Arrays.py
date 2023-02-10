class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
            
        left,right = 0,len(nums1)-1
        half = (len(nums1) + len(nums2))//2
        
        while True:
            
            mid1 = (left + right)//2
            mid2 = half - mid1 - 2
            
            mid1Left = nums1[mid1] if mid1 >= 0 else float('-inf')
            mid1Right = nums1[mid1+1] if mid1 < len(nums1)-1 else float ('inf')
            mid2Left  = nums2[mid2] if mid2 >= 0 else float('-inf')
            mid2Right = nums2[mid2+1] if mid2 < len(nums2)-1 else float ('inf')
                
            if mid1Left <= mid2Right and mid2Left <= mid1Right:
                if (len(nums1) + len(nums2))%2:
                    return min(mid1Right, mid2Right)
                else:
                    mid = (max(mid1Left, mid2Left) + min(mid1Right, mid2Right))/2
                    return mid
                
            if mid1Left > mid2Right:
                right = mid1-1
            else:
                left = mid1+1