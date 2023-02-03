    def __init__(self, w: List[int]):
        self.prefix = []
        curr = 0
        for weight in w:
            curr += weight
            self.prefix.append(curr)
        self._sum = curr

    def pickIndex(self) -> int:
        pick = self._sum * random.random()
        for i, curr in enumerate(self.prefix):
            if pick < curr:
                return i
