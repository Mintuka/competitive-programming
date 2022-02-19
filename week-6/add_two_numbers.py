# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res,prev = l1,l1
        
        while l1 and l2:
            calc   = l1.val + l2.val + carry
            l1.val = calc%10
            carry  = calc//10
            prev   = l1
            l1 = l1.next
            l2 = l2.next
            
        while l1 and not l2:
            calc    = l1.val + carry
            l1.val  = calc%10
            carry   = calc//10
            prev = l1
            l1   = l1.next
            
            
        while l2 and not l1:
            calc        = l2.val + carry
            prev.next   = ListNode(calc%10,None)
            carry       = calc//10
            prev = prev.next
            l2   = l2.next
            
        if carry: prev.next = ListNode(carry,None)
            
        return res