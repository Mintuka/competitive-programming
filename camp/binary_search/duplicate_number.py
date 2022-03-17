class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            current = abs(num)
            if nums[current] < 0: duplicate = current
            nums[current] = -nums[current]
            
        return duplicate