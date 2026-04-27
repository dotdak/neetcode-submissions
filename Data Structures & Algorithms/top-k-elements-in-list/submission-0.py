class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counter = sorted(counter, key=lambda x: counter[x], reverse=True)
        return sorted_counter[:k]