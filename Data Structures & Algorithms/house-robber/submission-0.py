class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0, 0, 0] + nums + [0, 0]
        for i in range(3, len(nums)):
            nums[i] = nums[i] + max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2]) 