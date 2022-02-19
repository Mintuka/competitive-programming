# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    dicn = {}
    while head:
        if head in dicn: return 1
        else: dicn[head] = head 
        head = head.next
    return 0