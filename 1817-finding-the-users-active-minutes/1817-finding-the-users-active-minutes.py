class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        UAM = defaultdict(set)
        users = [0 for _ in range(k)]
        for ID,Time in logs:
            UAM[ID].add(Time)
        for key,val in UAM.items():
            if len(val) <= k:
                users[len(val)-1] += 1
            
        return users 