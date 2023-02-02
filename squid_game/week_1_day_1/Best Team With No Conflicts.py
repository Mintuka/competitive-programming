class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        size = len(scores)
        
        team = []        
        for i in range(size):
            team.append((ages[i],scores[i]))
        team.sort()
        dp = [team[i][1] for i in range(size)]

        for i in range(size):
            for j in range(i):
                if team[i][1] >= team[j][1]:
                    dp[i] = max(dp[i], team[i][1] + dp[j])
        
        return max(dp)