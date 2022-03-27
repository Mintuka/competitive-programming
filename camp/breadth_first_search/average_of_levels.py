# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        average,answer = deque([root]),[]
        while average:
            size,Sum = len(average),0
            
            for i in range(size):
                popped = average.popleft()
                Sum += popped.val
                if popped.left: average.append(popped.left)
                if popped.right: average.append(popped.right)
                    
            answer.append(round(Sum/size,5))
            
        return answer