# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        previous,current = None,slow
        while current:
            nxt = current.next
            current.next = previous
            previous = current 
            current = nxt
            
        maxSum = 0
        while previous and head:
            maxSum = max(maxSum,previous.val + head.val)
            previous    = previous.next
            head        = head.next
            
        return maxSum