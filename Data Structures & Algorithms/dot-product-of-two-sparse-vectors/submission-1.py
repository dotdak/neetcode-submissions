from collections import OrderedDict
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.inx = OrderedDict()
        for k, num in enumerate(nums):
            if num == 0:
                continue
            self.inx[k] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        s = 0
        for k in self.inx:
            n1 = self.inx[k]
            n2 = vec.inx.get(k, 0)
            s += n1 * n2
        return s
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
