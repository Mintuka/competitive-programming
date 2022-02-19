class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(i):
            l,r = 0,i
            while l < r:
                arr[l],arr[r] = arr[r],arr[l]
                l += 1
                r -= 1
        k = []
        index = len(arr)
        while index > 0:
            if arr[index - 1] != index and index > 0:
                k.append(arr.index(index) + 1)
                flip(arr.index(index))
                k.append(index)
                flip(index - 1)
                
            index -= 1
        
        return k