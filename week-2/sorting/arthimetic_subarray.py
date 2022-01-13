def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:        
    result = [True]*len(r)
        
    for m in range(len(r)):
        size = r[m] - l[m] + 1
        temp = [0]*size
        
        j = 0
        for i in range(l[m],r[m]+1):
            temp[j] = nums[i]
            j += 1
        temp.sort()
        
        seq = temp[1] - temp[0]
        
        for i in range(2,size):
            if temp[i] - temp[i-1] != seq:
                result[m] = False
                break
            elif i == len(temp) - 1:
                result[m] = True
                
    return result