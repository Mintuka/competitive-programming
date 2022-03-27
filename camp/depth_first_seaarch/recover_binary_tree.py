# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:


    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.previous,self.predecessor,self.successor = None,None,None
        def inorder(root):
            if not root: return

            inorder(root.left)

            if self.previous and root.val < self.previous.val and not self.predecessor:
                self.predecessor = self.previous
            
            if self.previous and root.val < self.previous.val and self.predecessor:
                self.successor = root
                
            self.previous = root

            inorder(root.right)

        inorder(root)
        
        
        if self.predecessor and self.successor:
            self.predecessor.val,self.successor.val = self.successor.val,self.predecessor.val