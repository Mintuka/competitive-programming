class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #interate over the string from left to right
        #create deque which saves the digits to be returned
        #push char of the string into the deque
        #if current char is lessthan back of deque and k>0 pop and push the char
        #then increase the loop by 1 and decrease k by 1
        #elif k == 0 split the remaining substring and append them to the deque
        #zero is an edge case here if the deque contains only zero and if there exist leading zero
        n = len(num)
        d = deque([num[0]])
        for i in range(1,n):
            while k and d and num[i] < d[-1]:
                if d: d.pop() 
                k -= 1
            d.append(num[i])
        
        while d and k:
            d.pop()
            k -= 1
        
        count = Counter(d)
        if count['0'] == len(d): return "0"
        while d and d[0] == "0":
            d.popleft()
        
        return "".join(d)