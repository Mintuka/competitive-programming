class Node:
    
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size  = capacity
        self.cache = {}
        self.right = Node(-1,0)
        self.left  = Node(-1,0)
        self.right.prev = self.left
        self.left.nxt   = self.right
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        #insert into cache
        self.cache[key] = Node(key,value)
        #insert it in right
        self.insert(self.cache[key])
        if len(self.cache) > self.size:
            LRU = self.left.nxt
            del self.cache[LRU.key]
            self.remove(LRU)    
            
    def remove(self, node):
        prev,nxt = node.prev,node.nxt
        prev.nxt = nxt
        nxt.prev = prev
        
    def insert(self, node):
        prev = self.right.prev
        prev.nxt = node
        self.right.prev = node
        node.prev = prev
        node.nxt = self.right