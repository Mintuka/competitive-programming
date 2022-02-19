# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast,slow = head,head
        i = 0
        while i < n and fast:
            fast = fast.next
            i += 1
            
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        if slow == head and fast == None: head = head.next
        elif slow.next: slow.next = slow.next.next
        return head