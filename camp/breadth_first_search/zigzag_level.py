# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        queue,zigzagList = deque([root]),[]
        level = 0
        while queue:
            size = len(queue)
            levelList,poppedList = [],deque()
            for _ in range(size):
                if level%2:
                    popped = queue.pop()
                    levelList.append(popped.val)
                    if popped.right: poppedList.appendleft(popped.right)
                    if popped.left: poppedList.appendleft(popped.left)
                else:                    
                    popped = queue.popleft()
                    levelList.append(popped.val)
                    if popped.left: poppedList.append(popped.left)
                    if popped.right: poppedList.append(popped.right)

            queue.extend(poppedList)
            zigzagList.append(levelList)
            level += 1
            
        return zigzagList