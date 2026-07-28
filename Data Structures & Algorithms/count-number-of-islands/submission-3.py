class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ROWS, COLS = len(grid), len(grid[0])
        # visited = set()
        # moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        # def dfs(grid, r, c, visited):
        #     if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0' or (r, c) in visited:
        #         return 0
        #     # if r == ROWS - 1 and c == COLS - 1:
        #     #     return grid[r][c] == '1'
        #     visited.add((r,c))
        #     for dr, dc in moves:
        #         dfs(grid, r + dr, c + dc, visited)
        #     return 1

        # count = 0
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         count += dfs(grid, r, c, visited)

        # return count

        ROWS, COLS = len(grid), len(grid[0])
        moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        def dfs(r, c): 
            if not 0 <= r < ROWS or not 0 <= c < COLS:
                return False
            if grid[r][c] == '0':
                return False
            grid[r][c] = '0'
            for dr, dc in moves:
                dfs(r + dr, c + dc)

            return True

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c):
                    ans += 1
        return ans
        
        