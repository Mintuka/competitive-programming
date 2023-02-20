class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        query = queryIP.split('.')
        
        if len(query) == 4:
            for val in query:
                if len(val) > 1 and val[0] == '0':
                    return "Neither"
                if not val.isdigit() or int(val) < 0 or int(val) > 255:
                    return "Neither"
            return "IPv4"
    
        query = queryIP.split(':')
        # print(query)
        if len(query) == 8:
            for val in query:
                # print(len(val),val)
                if len(val) > 4 or len(val) < 1:
                    return "Neither"
                for c in val:
                    if c not in "0123456789abcdefABCDEF":
                        return "Neither"
            return "IPv6"
        
        return "Neither"