# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head
        mid   = self.getMid(head)
        left  = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)
    
    def getMid(self,head):
        slow,fast = None,head
        while fast and fast.next:
            if slow: slow = slow.next
            else: slow = head
            fast = fast.next.next
        
        mid,slow.next = slow.next,None
        
        return mid
    
    def merge(self,list1,list2):
        if list1 == None: return list2
        if list2 == None: return list1
        
        if list1.val <= list2.val:
            list1.next = self.merge(list1.next,list2)
            return list1
        else: 
            list2.next = self.merge(list1,list2.next)
            return list2