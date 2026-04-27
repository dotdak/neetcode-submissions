class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647 
        ROWS, COLS = len(grid), len(grid[0])
        moves = [(1,0), (0, 1), (0, -1), (-1, 0)]
        
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        distance = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = min(grid[r][c], distance)
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                        queue.append((nr, nc))
            distance += 1