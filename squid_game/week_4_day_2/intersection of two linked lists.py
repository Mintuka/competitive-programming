# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1,h2 = headA,headB
        len1,len2 = 0,0
        
        while h1:
            len1 += 1
            h1 = h1.next
        while h2:
            len2 += 1
            h2 = h2.next
         
        if len2 > len1:
            while len2 > len1:
                headB = headB.next
                len2 -= 1
        else:
            while len1 > len2:
                headA = headA.next
                len1 -= 1
        
        while headA and headB:
            if headA and headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
        
        