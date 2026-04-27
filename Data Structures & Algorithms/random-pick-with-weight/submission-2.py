import random

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for val in w:
            total += val
            self.prefix.append(total)
    def pickIndex(self) -> int:
        target = random.random() * self.prefix[-1]
        l, r = 0, len(self.prefix) - 1
        while l < r:
            mid = (l + r) // 2
            if self.prefix[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()