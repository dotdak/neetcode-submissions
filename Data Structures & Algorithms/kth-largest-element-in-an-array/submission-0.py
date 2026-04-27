import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > k:
                max_heap.remove(max(max_heap))
        return -max(max_heap)