# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,tilt):
            
            if not node: return (0,0)
            left  = dfs(node.left,tilt)
            right = dfs(node.right,tilt)
            
            totSum  = left[0]+right[0]+node.val
            tilt    = abs(left[0] - right[0]) + left[1] + right[1]
            return (totSum,tilt)
        
        return dfs(root,0)[1]