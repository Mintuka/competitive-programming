class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #look for courses with no pre-requisites on no dependencies
        #initialize the queue with them
        #remove a pre-requisite from the queue
        #decrement the indegree of other courses waiting for the removed pre-requisite
        #if neighbours of removed pre-requisite indegree goes down to zero add them to queue
        
        indegree = [0]*numCourses
        outgoing = defaultdict(set)
        queue = deque()
        
        for course,pre in prerequisites:
            
            indegree[course] += 1
            outgoing[pre].add(course)
            
        for i in range(numCourses):
            
            if indegree[i] == 0:
                queue.append(i)
            
        finished = 0
        while queue:
            
            pre = queue.popleft()
            finished  += 1
            
            for course in outgoing[pre]:
                
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
                    
        return finished == numCourses