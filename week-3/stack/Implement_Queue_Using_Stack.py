class MyQueue:

        def __init__(self):
            self.list = []        

        def push(self, x: int) -> None:
            self.list.append(x)
            
        def pop(self) -> int:
            if not self.empty():
                return self.list.pop(0)

        def peek(self) -> int:
            if not self.empty():
                return self.list[0]

        def empty(self) -> bool:
            if len(self.list):
                return False
            else:
                return True