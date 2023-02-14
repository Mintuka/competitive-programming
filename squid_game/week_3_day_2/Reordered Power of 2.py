class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(32):
            num = 1<<i
            num = str(num)
            num = [char for char in num]
            num.sort()
            num = "".join(num)
            n = str(n)
            n = [char for char in n]
            n.sort()
            n = "".join(n)
            
            if num == n:
                return True
            
        return False