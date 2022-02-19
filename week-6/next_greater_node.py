# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nodes = deque()
        while head: 
            nodes.append(head.val)
            head = head.next
        n = len(nodes)
        res,mono = [0]*n,deque()
        for i in range(n-1,-1,-1):
            while mono and nodes[i] >= nodes[mono[-1]]:
                mono.pop()
            if mono: res[i] = nodes[mono[-1]]
            mono.append(i)
        
        return res