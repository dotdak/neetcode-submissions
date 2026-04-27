import random

class Solution:
    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.prob = [0] * 10000
        index = 0
        for k, val in enumerate(w):
            inx_range = val*10000 // self.total
            for i in range(index, index+inx_range):
                self.prob[i] = k
        for i in range(index, len(w)):
            self.prob[i] = w[-1]
    def pickIndex(self) -> int:
        random_index = random.randint(0, 9999)
        return self.prob[random_index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()