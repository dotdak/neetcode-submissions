from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            indexes.setdefault(nums[i], []).append(i)
        ans = []
        for num in nums:
            if num in indexes and target - num in indexes:
                if num == target - num:
                    if len(indexes[num]) > 1:
                        return indexes[num][:2]
                    else:
                        continue
                return [indexes[num][0], indexes[target-num][0]]
        
        return []
                