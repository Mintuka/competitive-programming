class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isPredecessor(wordOne, wordTwo):
            i = j = 0
            while i < len(wordOne) and j < len(wordTwo):
                if wordOne[i] == wordTwo[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return i <= len(wordOne) and j == len(wordTwo)
        
        words = [(len(word),word) for word in words]
        words.sort()
        words = [word[1] for word in words]
        
        dp = [1 for i in range(len(words))]
        for i in range(len(words)):
            for j in range(i):
                if len(words[i]) - len(words[j]) == 1 and isPredecessor(words[i],words[j]):
                    dp[i] = max(dp[i], dp[j]+1)
         
        return max(dp)
                        