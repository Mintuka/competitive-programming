class RecentCounter:

    def __init__(self):
        self.counter = []
        self.previous= []
        self.min = 0

    def ping(self, t: int) -> int:
        if not len(self.counter):
            self.counter.append(t)
            self.previous.append(1)
            return 1
        else:
            i = len(self.counter) - 1
            if t - 3000 <= self.counter[self.min]:
                self.counter.append(t)
                p = self.previous[i]
                self.previous.append(p + 1)
                return p + 1
            elif t - 3000 > self.counter[self.min]:
                while t - 3000 > self.counter[self.min]:
                    self.min += 1
                    if self.min == len(self.counter):
                        break
                print("min",self.min," t",t," i",i)
                self.counter.append(t)
                r = len(self.counter) - self.min
                self.previous.append(r)
                return r
            elif i == len(self.counter) - 1:
                self.counter.append(t)
                self.previous.append(1)
                return 1
                   
            i += 1