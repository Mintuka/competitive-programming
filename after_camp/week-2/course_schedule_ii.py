class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0]*numCourses
        outgoing = defaultdict(set)
        queue    = deque()
        orders   = []
        
        for course,pre in prerequisites:
            
            indegree[course] += 1
            outgoing[pre].add(course)
            
        for i in range(numCourses):
            
            if indegree[i] == 0:
                queue.append(i)
            
        while queue:
            
            pre = queue.popleft()
            orders.append(pre)
            
            for course in outgoing[pre]:
                
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
                    
        return orders if len(orders) == numCourses else []
            