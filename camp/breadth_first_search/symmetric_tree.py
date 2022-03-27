# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left,right = deque([root.left]),deque([root.right])
        while left and right:
            poppedLeft  = left.popleft() 
            poppedRight = right.popleft()
            
            if poppedLeft and poppedRight and poppedLeft.val != poppedRight.val: return False
            if poppedLeft or poppedRight:
                if (poppedLeft and not poppedRight) or (not poppedLeft and poppedRight): return False
                left.extend([poppedLeft.right,poppedLeft.left])
                right.extend([poppedRight.left,poppedRight.right])
        
        return True