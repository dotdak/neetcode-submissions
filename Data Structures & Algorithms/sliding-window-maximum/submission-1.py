import bisect
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        current_max = max(nums[:k])
        ans.append(current_max)
        if len(nums) <= k:
            return ans
        
        windows = sorted(nums[:k])
        print(windows)
        for i in range(1, len(nums) - k + 1):
            # ans.append(max(nums[i:i+k]))
            prev_inx = bisect.bisect_left(windows, nums[i-1])
            windows.pop(prev_inx)
            inx = bisect.insort(windows, nums[i + k - 1])
            ans.append(windows[-1])
        return ans
