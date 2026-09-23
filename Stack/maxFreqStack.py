class FreqStack:

    def __init__(self):
        self.maxFreq = 0
        self.valToFreq = defaultdict(int)
        self.freqToVals = defaultdict(list)

    def push(self, val: int) -> None:
        self.valToFreq[val] += 1
        self.freqToVals[self.valToFreq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.valToFreq[val])

    def pop(self) -> int:
        val = self.freqToVals[self.maxFreq].pop()
        self.valToFreq[val] -= 1
        self.maxFreq = (self.maxFreq if self.freqToVals[self.maxFreq] else self.maxFreq - 1)
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()