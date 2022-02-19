class MinStack:

    def __init__(self):
        self.list = []        

    def push(self, val: int) -> None:
        self.list.append(val)

    def pop(self) -> None:
        self.list.pop()
        print(self.list)

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        temp = self.list.copy()
        temp.sort()
        return temp[0]