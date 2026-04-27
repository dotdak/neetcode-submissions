class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        window = set()
        length = 1
        L = 0
        for R in range(len(s)):
            while s[R] in window:
                window.discard(s[L])
                L += 1
            window.add(s[R])
            length = max(length, len(window))

        return length