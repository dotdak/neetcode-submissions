from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def levenstein(m, n):
            if m == 0:
                return n
            if n == 0:
                return m
            
            if word1[m-1] == word2[n-1]:
                return levenstein(m-1, n-1)
            
            return 1 + min(
                levenstein(m, n-1), 
                min(
                    levenstein(m-1, n), 
                    levenstein(m-1, n-1)
                )
            )
        return levenstein(len(word1), len(word2))