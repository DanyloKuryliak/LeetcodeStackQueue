import collections

class FreqStack:
    
    def __init__(self):
        self.elem_freq = collections.Counter()
        self.freq_stack = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val):
        self.elem_freq[val] += 1
        curr_freq = self.elem_freq[val]
        self.max_freq = max(self.max_freq, curr_freq)
        self.freq_stack[curr_freq].append(val)

    def pop(self):
        val = self.freq_stack[self.max_freq].pop()
        if not self.freq_stack[self.max_freq]:
            self.max_freq -= 1
        self.elem_freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()