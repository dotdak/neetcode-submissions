import copy
import heapq
import bisect
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        windows = [(-num, inx) for inx, num in enumerate(nums[:k])]
        heapq.heapify(windows)
        ans.append(-windows[0][0])
        for i in range(k, len(nums)):
            # ans.append(max(nums[i:i+k]))
            # prev_inx = bisect.bisect_left(windows, nums[i-1])
            # windows.pop(prev_inx)
            # inx = bisect.insort(windows, nums[i + k - 1])
            # ans.append(windows[-1])
            heapq.heappush(windows, (-nums[i], i))
            while windows[0][1] <= i - k:
                heapq.heappop(windows)
            ans.append(-windows[0][0])

        return ans
