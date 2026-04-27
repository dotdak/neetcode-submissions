class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalin(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        count = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if isPalin(s[i:j]):
                    count += 1
        return count