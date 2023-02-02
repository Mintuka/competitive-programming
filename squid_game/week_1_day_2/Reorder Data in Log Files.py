class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        _list = [val.split(' ') for val in logs]
        digit = [val for val in _list if val[1].isdigit()]
        words = [[val[0],' '.join(val[1:])] for val in _list if not val[1].isdigit()]
        words.sort()
        words.sort(key=lambda x:x[1])
        words = [' '.join(val) for val in words]
        digits = [' '.join(val) for val in digit]
        return words + digits