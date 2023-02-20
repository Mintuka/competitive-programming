class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        _max = nums[-1]
        max_diff = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < _max:
                max_diff = max(max_diff, _max - nums[i])
            if nums[i] > _max:
                _max = nums[i]
        return max_diff
                