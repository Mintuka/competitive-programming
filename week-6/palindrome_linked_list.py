# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        previous,current = None,slow
        while current:
            nxt          = current.next
            current.next = previous
            previous     = current
            current      = nxt
            
        while previous and head:
            if previous.val != head.val: return False
            previous,head = previous.next,head.next
            
        return True