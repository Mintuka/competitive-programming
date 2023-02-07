class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = 0
        for log in logs:
            if log[:2] == '..':
                if ops:
                    ops -= 1
            elif log[:2] != './':
                ops += 1
        return ops