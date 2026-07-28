class RandomizedSet:

    def __init__(self):
        self.inx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.inx:
            return False
        self.inx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.inx:
            return False
        i = self.inx[val]
        last = self.nums[-1]
        self.nums[i] = last
        self.inx[last] = i 
        self.nums.pop()
        del self.inx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()