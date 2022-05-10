class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(set)
        
        for pre,course in prerequisites:
            graph[pre].add(course)
            
        def dfs(pre):
            
            visited.add(pre)
            connected = set()
            
            for course in graph[pre]:
                if course not in visited:
                    connected |= dfs(course)
                else:
                    connected |= checkList[course]
                    
                connected.add(course)
                
            checkList[pre] = connected
            
            return connected
        
        visited,checkList = set(),[0]*numCourses
        
        for pre in range(numCourses):
            if pre not in visited:
                dfs(pre)
             
        answer = []
        for pre,course in queries:
            if course in checkList[pre]:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer
                