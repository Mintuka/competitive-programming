class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s,i):
            encoded = ""  #this str must die after it transfers to parent function
            while i < len(s):
                if s[i] == ']': return (encoded,i+1)
                k = deque()
                if (re.match('\d',s[i])):
                    while re.match('\d',s[i]):
                        k.append(s[i])
                        i += 1
                    i += 1

                    v = decode(s,i)
                    encoded += v[0] * int("".join(k))  #add previous str onto current str mul of k
                    i = v[1]
                else:
                    encoded += s[i]
                    i += 1                
            return (encoded,i)[0]
        
        i = 0
        return decode(s,i)