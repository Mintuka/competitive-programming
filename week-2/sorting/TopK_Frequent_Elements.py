class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for x in nums:
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
        
        elements = [0]*k
        i = len(freq) - 1
        j = 0
        while j < k:
            elements[j] = freq[i][0]
            i -= 1
            j += 1
        
        
        return elements