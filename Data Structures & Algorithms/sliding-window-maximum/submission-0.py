class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        current_max = max(nums[:k])
        ans.append(current_max)
        if len(nums) <= k:
            return ans
        
        # windows = nums[:k]
        for i in range(1, len(nums) - k + 1):
            ans.append(max(nums[i:i+k]))
        return ans
