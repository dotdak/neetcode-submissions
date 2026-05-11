from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            n1 = nums[i]
            n2 = target - nums[i]
            if n2 in indexes:
                return [indexes[n2], i]
            indexes[n1] = i