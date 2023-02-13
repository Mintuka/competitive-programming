class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        pre_sum = [val for val in nums]
        for idx in range(1,len(nums)):
            pre_sum[idx] += pre_sum[idx-1]
            
        tot = 0
        sub_count = defaultdict(int)
        sub_count[0] = 1
        for _sum in pre_sum:
            remainder = _sum%k
            tot += sub_count[remainder]
            sub_count[remainder] += 1
            
        return tot