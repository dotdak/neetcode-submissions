class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in counter:
            buckets[counter[num]].append(num)
        ans = []
        inx = len(nums)
        while len(ans) < k:
            if len(buckets[inx]) > 0:
                ans.extend(buckets[inx])
            inx -= 1
        return ans[:k]
