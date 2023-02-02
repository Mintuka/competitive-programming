class Solution:
    def numberOfWays(self, s: str) -> int:
        left_ones = [0 for i in range(len(s))]
        right_zeros = [0 for i in range(len(s))]
        left_zeros = [0 for i in range(len(s))]
        right_ones = [0 for i in range(len(s))]
        
        ones,zeros = 0,0
        for idx,num in enumerate(s):
            left_zeros[idx] = zeros
            left_ones[idx] = ones
            if num == '0':
                zeros += 1
            else:
                ones += 1
                
        ones,zeros = 0,0
        a = [s[i] for i in range(len(s)-1,-1,-1)]
        # print(a)
        for idx,num in enumerate(a):
            right_zeros[idx] = zeros
            right_ones[idx] = ones
            if num == '0':
                zeros += 1
            else:
                ones += 1
                
        ways = 0
        right_zeros = right_zeros[::-1]
        right_ones = right_ones[::-1]
        # print(left_ones,right_ones,left_zeros,right_zeros)
        for i in range(1,len(s)-1):
            if s[i] == '0':
                # print(i, left_ones[i] * right_ones[i])
                ways += left_ones[i] * right_ones[i]
            else:
                # print(i,left_zeros[i] * right_zeros[i])
                ways += left_zeros[i] * right_zeros[i]
                
        return ways