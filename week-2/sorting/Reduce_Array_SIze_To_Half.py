class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dictionary = {}
        for x in arr:
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1
                
        freq = []
        for key,value in dictionary.items():
            freq.append([key,value])
            
        #use merge sort
        def sort(A,lo,hi,aux):
            if hi <= lo: return
            mid = math.floor(lo + (hi - lo)/2)
            sort(A,lo,mid,aux)
            sort(A,mid+1,hi,aux)
            merge(A,lo,mid,hi,aux)

        def merge(A,lo,mid,hi,aux):
                i=lo 
                j=mid+1
                for k in range(lo,hi+1):
                    aux[k] = A[k]
                for k in range(lo,hi+1):
                    if(i > mid ):
                        A[k] = aux[j]
                        j += 1
                    elif j > hi:
                        A[k] = aux[i]
                        i += 1
                    elif aux[j][1] < aux[i][1]:
                        A[k] = aux[j]
                        j += 1
                    else: 
                        A[k] = aux[i]
                        i += 1

        aux = [0]*len(freq)
        sort(freq,0,len(freq)-1,aux)
        
        size = 0
        count, half = 0,len(arr)//2
        
        i = len(freq) - 1
        while count < half:
            if freq[i][1] == 2 * half:
                return 1
            
            else:
                count += freq[i][1]
                size += 1
            i -= 1
        return size