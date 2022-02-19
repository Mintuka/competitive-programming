# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None): return
        elif(head.next == None): return head
        head,head.next,head.next.next = head.next,head,head.next.next
        head.next.next = self.swapPairs(head.next.next)        
        return head