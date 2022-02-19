class MyCircularDeque:

    def __init__(self, k: int):
        self.list = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.list) < self.k:
            self.list.insert(0,value)
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if len(self.list) < self.k:
            self.list.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.list.pop(0)
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.list.pop()
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.list[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.list[-1]

    def isEmpty(self) -> bool:
        if len(self.list):
            return False
        else:
            return True

    def isFull(self) -> bool:
        if len(self.list) == self.k:
            return True
        else:
            return False