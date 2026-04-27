class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i

        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j
        
        for m in range(len(word1)-1,-1,-1):
            for n in range(len(word2)-1,-1,-1):
                if word1[m] == word2[n]:
                    dp[m][n] = dp[m+1][n+1]
                else:
                    dp[m][n] = 1 + min(
                       dp[m][n+1], 
                        min(
                            dp[m+1][n], 
                            dp[m+1][n+1]
                        )
                    )

        return dp[0][0]