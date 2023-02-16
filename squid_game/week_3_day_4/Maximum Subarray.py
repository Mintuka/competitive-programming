class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current,_max = 0,-inf
        for num in nums:
            current = max(current + num, num)
            _max = max(_max,current)
        return _max