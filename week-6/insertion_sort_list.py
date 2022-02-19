# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        insert  = ListNode(0,None)
        iterate = head
        while iterate != None:
            nextIteration   = iterate.next
            insertPrv       = insert
            insertNxt       = insert.next
            
            while insertNxt:
                if insertNxt.val > iterate.val: break
                insertPrv = insertPrv.next
                insertNxt = insertNxt.next

            iterate.next    = insertNxt
            insertPrv.next  = iterate
            iterate         = nextIteration
        
        return insert.next