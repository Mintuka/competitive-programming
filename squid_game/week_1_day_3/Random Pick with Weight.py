import bisect
import random 
class Solution:

    def __init__(self, w: List[int]):
        self.prefixsum = [0]

        for num in w:
            self.prefixsum.append(self.prefixsum[-1] + num)
        self.totalSum = self.prefixsum[-1]

    def pickIndex(self) -> int:
        randomNum = random.randint(1, self.totalSum)
        idx = bisect.bisect_left(self.prefixsum, randomNum)
        return idx-1 


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()