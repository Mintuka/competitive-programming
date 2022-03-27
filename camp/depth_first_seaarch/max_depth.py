"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(parent,maxHeight,currentHeight):
            currentHeight += 1 
            maxHeight = max(maxHeight,currentHeight)
            for child in parent.children:
                value = dfs(child,maxHeight,currentHeight)
                maxHeight = max(maxHeight,value)
            return maxHeight
        
        
        maxDepth,currentDepth = 0,0
        return dfs(root,maxDepth,currentDepth) if root else 0