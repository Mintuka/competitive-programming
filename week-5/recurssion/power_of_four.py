class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n <= 0 else False if math.log(abs(n),2)%math.log(4,2) else True