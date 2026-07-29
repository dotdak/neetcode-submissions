import bisect
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return
        inx = bisect.bisect_left(self.nums, num)
        self.nums.insert(inx, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2:
            return self.nums[n//2]
        else:
            return (self.nums[n // 2 - 1] + self.nums[n//2]) / 2 
        