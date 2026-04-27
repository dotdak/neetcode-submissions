import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick(l, r):
            pivot = nums[l]
            p = r
            for i in range(r, l, -1):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p -= 1
            nums[p], nums[l] = nums[l], nums[p]
            if p > k - 1:
                return quick(l, p - 1)
            elif p < k - 1:
                return quick(p + 1, r)
            else:
                return nums[p]
        return quick(0, len(nums) - 1)