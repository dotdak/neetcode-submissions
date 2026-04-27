class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def levenstein(word1, word2, m, n):
            if m == 0:
                return n
            if n == 0:
                return m
            
            if word1[m-1] == word2[n-1]:
                return levenstein(word1, word2, m-1, n-1)
            
            return 1 + min(
                levenstein(word1, word2, m, n-1), 
                min(
                    levenstein(word1, word2, m-1, n), 
                    levenstein(word1, word2, m-1, n-1)
                )
            )
        return levenstein(word1, word2, len(word1), len(word2))