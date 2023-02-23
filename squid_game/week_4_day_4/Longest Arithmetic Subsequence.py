class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        dp = defaultdict(list)
        for i in range(len(nums)):
            dp[i] = [0 for i in range(501)]
            
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] >= nums[j]:
                    gap = nums[j] - nums[i]
                    dp[i][gap] = dp[j][gap] + 1
        
        _max = 0
        for values in dp.values():
            _max = max(_max, max(values))
            
            
        nums = nums[::-1]
        
        dp = defaultdict(list)
        for i in range(len(nums)):
            dp[i] = [0 for i in range(501)]
            
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] >= nums[j]:
                    gap = nums[j] - nums[i]
                    dp[i][gap] = dp[j][gap] + 1
        
        for values in dp.values():
            _max = max(_max, max(values))
            
        return _max+1