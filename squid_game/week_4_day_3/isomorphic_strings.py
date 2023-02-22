class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        visited = defaultdict(str)
        for i in range(len(s)):
            if s[i] in visited:
                if visited[s[i]] != t[i]:
                    return False
            else:
                visited[s[i]] = t[i]
				
        if len(set(visited.values())) != len(visited.values()): 
            return False    
        return True