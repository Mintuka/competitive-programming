class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(list)
        for idx,num in enumerate(nums):
            count[num].append(idx)
        mn = float('inf')
        mx = 0
        
        for val in count.values():
            mx = max(mx, len(val))
        
        for key,val in count.items():
            if len(val) == mx:
                mx = len(val)
                print(val[-1] - val[0] + 1)
                mn = min(mn, val[-1] - val[0] + 1)
                
        return mn
        
        
        