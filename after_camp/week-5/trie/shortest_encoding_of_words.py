class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        node = self.root
        
        for char in word[::-1]:
            node = node.children[char]
            
        return len(word) + 1
    
    def search(self,word):
        
        node = self.root
        
        for char in word[::-1]:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return True
    
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        shortest_length = 0
        trie = Trie()
        words = [[len(word),word] for word in words]
        words = sorted(words,reverse=True)
        
        for size,word in words:
            if trie.search(word):
                continue
            shortest_length += trie.insert(word)
            
        return shortest_length