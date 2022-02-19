# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #compare head val of both lists
        #if list1 head val is lessthan list2 head val next of list1 will be minimum of next of list1 and head of list2
        #if list2 head val is lessthan list1 head val next of list2 will be minimum of next of list2 and head of list1
        #return the minimum of list1 and list2 when the recursion returns back
        #base case if list1 is None return list2 else if list2 is None return list1
        if list1 == None: return list2
        if list2 == None: return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2