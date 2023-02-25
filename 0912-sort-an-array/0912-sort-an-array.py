class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        mn = abs(min(nums))
        for i in range(len(nums)):
            nums[i] += mn
        # print(nums)
        mx = max(1,abs(max(nums)))
        digits = floor(math.log(mx,10)) + 1
        
        for d in range(digits):
            freq = [0 for _ in range(10)]
            for num in nums:
                div = num//(10**(d))
                mod = div%10   
                freq[mod] += 1
            # print(freq)
            for i in range(1,10):
                freq[i] += freq[i-1]
                
            temp = [0 for i in range(len(nums))]
            for idx,num in enumerate(nums[::-1]):
                div = num//(10**(d))
                mod = div%10
                temp[freq[mod]-1] = num
                freq[mod] -= 1
            # print('temp',temp)    
            nums = [val for val in temp]
        
        # print(nums)
        for i in range(len(nums)):
            nums[i] -= mn
            
        return nums