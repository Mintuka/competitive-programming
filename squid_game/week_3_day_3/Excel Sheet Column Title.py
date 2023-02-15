class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 26:
            if columnNumber%26:
                result.append(chr(64+columnNumber%26))
            else:
                result.append('Z')
                columnNumber -= 1
            columnNumber //= 26
        if columnNumber:
            result.append(chr(64+columnNumber))
        return ''.join(result[::-1])