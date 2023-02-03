# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)
        def dfs(node, col, row):
            if not node:
                return 
            columns[col].append((row,node.val))
            dfs(node.left, col-1, row+1)
            dfs(node.right, col+1, row+1)
         
        dfs(root, 0, 0)
        result =  sorted([(key,sorted(val)) for key,val in columns.items()])
        return [[v[1] for v in val[1]] for val in result]
            