class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        _sorted = sorted([int(n) for n in num])[::-1]
        for i in range(len(num)):
            if int(num[i]) != _sorted[i]:
                swap = num[i]
                num[i] = str(_sorted[i])
                for j in range(len(num)-1,i,-1):
                    if num[j] == num[i]:
                        num[j] = swap
                        break
                break
        return int(''.join(num))