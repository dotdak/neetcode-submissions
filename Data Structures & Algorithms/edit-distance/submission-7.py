class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0 for _ in range(len(word2) + 1)]
        nextDp = [0 for _ in range(len(word2) + 1)]
        for j in range(len(word2) + 1):
            dp[j] = len(word2) - j

        for m in range(len(word1)-1,-1,-1):
            nextDp[len(word2)] = len(word1) - m
            for n in range(len(word2)-1,-1,-1):
                if word1[m] == word2[n]:
                    nextDp[n] = dp[n+1]
                else:
                    nextDp[n] = 1 + min(
                       dp[n+1], 
                        min(
                            dp[n], 
                            nextDp[n+1]
                        )
                    )
            dp = nextDp[:]

        return dp[0]