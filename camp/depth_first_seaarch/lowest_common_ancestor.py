# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        bfsQueue,mapToParent = deque([root]),{}
        
        while bfsQueue:
            
            size = len(bfsQueue)
            
            ancestor = deque()
            
            for nodes in range(size):
                
                node = bfsQueue.popleft()
                ancestor.append(node)
                
                if node.left:
                    bfsQueue.append(node.left)
                    mapToParent[node.left] = node
            
                if node.right:
                    bfsQueue.append(node.right)
                    mapToParent[node.right] = node
                    
        visited = set()
        while len(ancestor) > 1:
            
            node = ancestor.popleft()
            
            if mapToParent[node] not in visited:
                visited.add(mapToParent[node])                
                ancestor.append(mapToParent[node])
            
        return ancestor[0]