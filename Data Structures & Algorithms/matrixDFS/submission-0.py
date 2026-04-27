class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(grid, r, c, visited):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == 1:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            visited.add((r, c))
            count = 0
            move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in move:
                count += dfs(grid, r+dr, c+dc, visited)
            visited.discard((r, c))
            return count 
        return dfs(grid, 0, 0, set())