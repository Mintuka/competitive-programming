class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        sub_target = defaultdict(str)
        for i in range(len(target)):
            sub_target[target[:i+1]] = target[i+1:]
        count = Counter(nums)
        
        pairs = 0
        for key,val in sub_target.items():
            if val in count and key in count:
                if val == key:
                    pairs += count[key]*(count[val]-1)
                else:
                    pairs += count[key]*count[val]

        return pairs