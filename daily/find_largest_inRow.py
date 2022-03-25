# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        rowsLargest,queue = [],deque()
        root and queue.append(root)
        
        while queue:
            
            size = len(queue)
            
            largest = -inf
            
            for nodes in range(size):
            
                node = queue.popleft()
                largest = max(largest,node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            rowsLargest.append(largest)
            
            
        return rowsLargest
                
        
        