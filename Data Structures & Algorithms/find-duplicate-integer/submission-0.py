class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p1 = p2 = nums[0]
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break
        p3 = nums[0]
        while p1 != p3:
            p1 = nums[p1]
            p3 = nums[p3]
        return p1