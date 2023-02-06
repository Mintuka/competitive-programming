class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0 for i in range(len(words))]
        
        for i,word in enumerate(words):
            prefix[i] = prefix[i-1]
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                prefix[i] += 1
        
        result = [0 for i in range(len(queries))]
        for i,(l,r) in enumerate(queries):
            result[i] = prefix[r]
            if l:
                result[i] -= prefix[l-1]
                
        return result