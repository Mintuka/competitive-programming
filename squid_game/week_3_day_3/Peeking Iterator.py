class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.nxt = 0
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.iterator[self.nxt]

    def next(self):
        """
        :rtype: int
        """
        nxt = self.nxt
        self.nxt += 1
        return self.iterator[nxt]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nxt < len(self.iterator):
            return True
        return False

ans = PeekingIterator([1,2,3])
ans.next()