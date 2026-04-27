class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        max_counter = max(counter.values())
        buckets = [[] for _ in range(max_counter + 1)]
        for num in counter:
            buckets[counter[num]].append(num)
        ans = []
        inx = max_counter
        while len(ans) < k:
            if len(buckets[inx]) > 0:
                ans.extend(buckets[inx])
            inx -= 1
        return ans[:k]
