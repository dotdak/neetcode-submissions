class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        max_freq = 0
        L = 0
        for R in range(len(s)):
            counter[s[R]] = 1 + counter.get(s[R], 0)
            max_freq = max(max_freq, counter[s[R]])
            while R - L + 1 - max_freq > k:
                counter[s[L]] -= 1
                L += 1
        return R - L + 1