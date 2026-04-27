import functools
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = 1
        # for r in range(m):
        #     dp[r][0] = 1

        # for c in range(n):
        #     dp[0][c] = 1

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0: continue
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]

        # @functools.cache
        # def dfs(r, c):
        #     if not 0 <= r < m or not 0 <= c < n:
        #         return 0
        #     if r == m - 1 and c == n - 1:
        #         return 1
        #     return dfs(r + 1, c) + dfs(r, c+1)
        # return dfs(0,0)