class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        def dfs(r, c):
            if min(r, c) < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0
            area = 1
            grid[r][c] = 0
            for dr, dc in moves:
                area += dfs(r+dr,c+dc)
            return area

        max_area = 0
        for r in range(m):
            for c in range(n):
                max_area = max(max_area, dfs(r, c))

        return max_area