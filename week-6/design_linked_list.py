class ListNode:
    def __init__(self,val=0,next=None):
        self.val    = val
        self.next   = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1
        iterate,findIndex = self.head,0
        
        while iterate:
            if findIndex == index: return iterate.val
            iterate = iterate.next
            findIndex += 1
            
    def addAtHead(self, val: int) -> None:
            self.head = ListNode(val,self.head)
            self.size += 1

    def addAtTail(self, val: int) -> None:
        iterate = self.head
        while iterate:
            if iterate.next == None: break
            iterate = iterate.next
        if iterate: iterate.next = ListNode(val,None)
        else: self.head = ListNode(val,None)
        self.size += 1
            
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: return
        if index == 0: 
            self.head = ListNode(val,self.head)
            self.size += 1
            
        else :
            iterate,findIndex = self.head,0
            while iterate: 
                if findIndex == index - 1: 
                    iterate.next = ListNode(val,iterate.next)
                    self.size += 1
                iterate = iterate.next
                findIndex += 1
            

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return
        if index == 0: 
            self.head = self.head.next
            self.size -= 1
        else:   
            iterate,findIndex = self.head,0
            while iterate: 
                if findIndex == index - 1:
                    iterate.next = iterate.next.next
                    self.size -= 1
                iterate = iterate.next
                findIndex += 1