class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        allIps = []
        def backtrack(i, currentIp):
            if len(currentIp) > 4:
                return
            if i == len(s):
                if len(currentIp) == 4:
                    allIps.append([v for v in currentIp])
                return
            for j in range(i+1,len(s)+1):
                if s[i:j] == '0':
                    backtrack(j, [v for v in currentIp]+['0'])
                elif s[i] != '0' and int(s[i:j]) <= 255:
                    backtrack(j, [v for v in currentIp]+[s[i:j]])
        
        backtrack(0,[])
        return ['.'.join(ip) for ip in allIps]