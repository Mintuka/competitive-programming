class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        size = len(nums)
        sum = [0]*(size+1)
        sum[0] = 0
        for i in range(size):
            sum[i+1] = sum[i] + nums[i]
                
        list = []
        mn   = math.inf
        for i in range(size+1):

            while len(list) and sum[i] - sum[list[0]]>= k:
                # mn = min(mn,i - list[0])
                if i - list[0] < mn:
                    mn = i - list[0]
                list.pop(0)

            while len(list) and sum[i] - sum[list[-1]] <= 0:
                list.pop()

            list.append(i)

            

        return mn if mn < math.inf else -1