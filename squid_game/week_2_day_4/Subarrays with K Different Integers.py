class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def countSubarrays(k):        
            count = defaultdict(int)        
            res = right = left = 0

            while right < len(nums):
                count[nums[right]] += 1
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                res += right - left + 1
                right += 1
            return res
        
        good_subarrays = countSubarrays(k) - countSubarrays(k-1)
        return good_subarrays