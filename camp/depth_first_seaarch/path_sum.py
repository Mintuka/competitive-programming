# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def rootToLeaf(node,targetSum,rootLeafSum):
            rootLeafSum += node.val
            left,right = False,False
            if node.left or node.right:
                if node.left:
                    left  = rootToLeaf(node.left,targetSum,rootLeafSum)
                if node.right:
                    right = rootToLeaf(node.right,targetSum,rootLeafSum)

                return left or right
            else:
                return targetSum == rootLeafSum 
        
        return rootToLeaf(root,targetSum,0) if root else False